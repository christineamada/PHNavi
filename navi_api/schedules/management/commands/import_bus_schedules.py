import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from schedules.models import BusSchedule

class Command(BaseCommand):
    help = 'Import bus schedules from a CSV file'

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    print(row, row['departure_time'], row['arrival_time'])
                    departure_time = self.convert_time_format(row['departure_time']) if row['departure_time'] else None
                    arrival_time = self.convert_time_format(row['arrival_time']) if row['arrival_time'] else None
                    fare = self.strip_currency_symbol(row['fare'])

                    BusSchedule.objects.create(
                        company_name=row['company_name'],
                        from_location=row['from_location'],
                        from_latitude=row['from_latitude'],
                        from_longitude=row['from_longitude'],
                        to_location=row['to_location'],
                        to_latitude=row['to_latitude'],
                        to_longitude=row['to_longitude'],
                        departure_time=departure_time,
                        arrival_time=arrival_time,
                        travel_class=row['travel_class'],
                        fare=fare,
                        travel_days=row['travel_days']
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error processing row: {row}. Error: {e}"))

        self.stdout.write(self.style.SUCCESS('Successfully imported bus schedules from CSV!'))

    def convert_time_format(self, time_str):
        print(time_str)
        if time_str:
            time_str = time_str.strip()  # Remove any extra spaces
            return datetime.strptime(time_str, '%I:%M %p').strftime('%H:%M:%S')
        return None

    def strip_currency_symbol(self, fare_str):
        return ''.join(filter(str.isdigit, fare_str))

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the CSV file')