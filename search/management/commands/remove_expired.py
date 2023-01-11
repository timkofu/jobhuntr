from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from search.models import JobsData


class Command(BaseCommand):
    help = "Remove entries older than x days"

    def handle(self, *args: ..., **options: ...) -> None:
        try:
            JobsData.objects.filter(
                added_on__lte=datetime.now() - timedelta(days=settings.MAX_JOB_AGE)
            ).delete()
        except Exception as e:
            raise CommandError(str(e))
