
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError

from search.models import JobsData


class Command(BaseCommand):
    help = "Remove entries older than 28 days"

    def handle(self, **options):
        try:
            JobsData.objects.filter(add_time__lte=datetime.now()-timedelta(days=28))
        except Exception as e:
            raise CommandError(e.message)

