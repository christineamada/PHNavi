import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from schedules.models import FerrySchedule

# TODO: Figure out why this isn't working
class Command(BaseCommand):
    help = 'Import ferry schedules from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    ferry_schedule = FerrySchedule.objects.create(
                        company_name=row.get('company_name'),
                        from_location=row.get('from_location'),
                        to_location=row.get('to_location'),
                        vessel=row.get('vessel'),
                        departure_time=row.get('departure_time'),
                        day_of_departure=row.get('day_of_departure'),
                        arrival_time=row.get('arrival_time'),
                        day_of_arrival=row.get('day_of_arrival'),
                        accommodation=row.get('accommodation'),
                        fare=row.get('fare')
                    )
                    self.stdout.write(self.style.SUCCESS(f"Successfully created FerrySchedule: {ferry_schedule}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Failed to import row: {row}. Error: {e}"))

        self.stdout.write(self.style.SUCCESS('Successfully imported ferry schedules'))
