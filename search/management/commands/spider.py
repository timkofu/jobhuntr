
import logging

import feedparser

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

        if job_sources:
            for js in job_sources:
                for feed in feedparser.parse(js.url)['entries']:
                    job_url = feed.get('link')
                    job_title = feed.get('title')
                    if job_url and job_title:
                        try:
                            JobsData(
                                url=job_url,
                                title=job_title,
                                source=js
                            ).save()
                        except IntegrityError:
                            pass
