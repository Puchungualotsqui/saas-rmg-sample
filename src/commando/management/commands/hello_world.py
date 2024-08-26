from django.core.management import BaseCommand
from typing import Any


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        print('Hello World')
