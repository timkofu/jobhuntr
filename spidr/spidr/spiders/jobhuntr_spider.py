
import urlparse

import django
django.setup()

from django.db import transaction

from scrapy.spiders import Spider
from search.models import SourceLinks
from search.models import JobsData

from feedparser import parse as feed_parser


class JobhuntrSpider(Spider):
    
    name = "jobhuntr"
    all_urls = SourceLinks.objects.all()
    allowed_domains = (urlparse.urlparse(u.url).hostname for u in all_urls)
    start_urls = (u.url for u in all_urls)
    
    def parse(self, response):

        with transaction.atomic():
            for feed in feed_parser(response.body)['entries']:

                job_url = feed.get('link')
                job_title = feed.get('title')

                if job_url and job_title:
                    JobsData.objects.get_or_create(
                        url=job_url,
                        title=job_title,
                        source=self.all_urls.get(url=response.url)
                    )
