# Generated by Django 5.1.2 on 2024-10-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_alter_busschedule_arrival_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='FerrySchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.CharField(max_length=255)),
                ('to_location', models.CharField(max_length=255)),
                ('vessel', models.CharField(max_length=100)),
                ('departure_time', models.TimeField()),
                ('day_of_departure', models.CharField(max_length=50)),
                ('arrival_time', models.TimeField(blank=True, null=True)),
                ('day_of_arrival', models.CharField(blank=True, max_length=50, null=True)),
                ('accommodation', models.CharField(max_length=50)),
                ('passenger_type', models.CharField(max_length=50)),
                ('fare', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
