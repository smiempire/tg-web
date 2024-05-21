import datetime

from django.core.management import BaseCommand
from pytz import timezone

from main.models import Flight


class Command(BaseCommand):

    def handle(self, *args, **options):
        pass
