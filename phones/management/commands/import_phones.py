import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Заполнение базы данных'
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.create(name=phone['name'],
                                 image=phone['image'],
                                 price=int(phone['price']),
                                 release_data=phone['release_date'],
                                 lte_exist=phone['lte_exists'],
                                 slug=self.slug(phone['name']))
            self.stdout.write(f'Телефон {phone["name"]} загружен')

    def slug(self, text):
        text = text.lower()
        count = text.count(' ')
        text = text.replace(' ', '-', count)
        return text
