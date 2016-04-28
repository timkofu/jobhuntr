
import logging

import gevent
from gevent.monkey import patch_socket
patch_socket()

import feedparser

from django.db import transaction
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from search.models import (
    SourceLinks,
    JobsData
)


class Command(BaseCommand):

    help = "Le Spiduer"

    def handle(self, **options):

        job_sources = SourceLinks.objects.all()  # # values_list("url", flat=True)

        def get_posts(job_source):

            feeds = feedparser.parse(job_source.url)['entries']

            with transaction.atomic():  # # Commits all entries in one transaction
                for feed in feeds:

                    job_url = feed.get('link')
                    job_title = feed.get('title')

                    if job_url and job_title:
                        try:
                            JobsData.objects.get_or_create(
                                url=job_url,
                                title=job_title,
                                source=job_source
                            )
                        except IntegrityError:
                            pass

        if job_sources:
            try:
                gevent.joinall(
                    [gevent.spawn(get_posts, url) for url in job_sources]
                )
            except Exception as e:
                logging.error(str(e))
