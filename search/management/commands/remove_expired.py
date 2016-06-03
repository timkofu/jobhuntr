
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError

from search.models import JobsData


class Command(BaseCommand):
    help = "Remove entries older than x days"

    def handle(self, **options):
        try:
            JobsData.objects.filter(added_on__lte=datetime.now()-timedelta(days=14)).delete()
        except Exception as e:
            raise CommandError(e.message)
