
import urlparse

from feedparser import parse as feed_parser
from scrapy.spider import Spider
from search.models import SourceLinks
from search.models import JobsData


class JobhuntrSpider(Spider):
    
    name = "jobhuntr"
    all_urls = SourceLinks.objects.all()
    allowed_domains = (urlparse.urlparse(u.url).hostname for u in all_urls)
    start_urls = (u.url for u in all_urls)
    
    def parse(self, response):
        
        for feed in feed_parser(response.body)['entries']:

            url = feed.get('link')
            title = feed.get('title')
            if url:
                # response.url has the url of the request
                source_url_object = self.all_urls.get(url=response.url)
            else:
                source_url_object = None

            if url and title and source_url_object:
                JobsData.objects.get_or_create(
                    url=url,
                    title=title,
                    source_url=source_url_object
                )
