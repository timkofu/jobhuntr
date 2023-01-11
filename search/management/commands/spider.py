import feedparser

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from search.models import SourceLinks, JobsData


class Command(BaseCommand):

    help = "Le Spiduer"

    def handle(self, *args: ..., **options: ...):

        try:

            job_sources = SourceLinks.objects.all()  # # values_list("url", flat=True)

            if job_sources:
                for js in job_sources:
                    for feed in feedparser.parse(js.url)["entries"]:  # type: ignore
                        job_url: str = feed.get("link")
                        job_title: str = feed.get("title")
                        if job_url and job_title:
                            try:
                                JobsData(url=job_url, title=job_title, source=js).save()
                            except IntegrityError:
                                pass
        except Exception as e:
            CommandError(str(e))
