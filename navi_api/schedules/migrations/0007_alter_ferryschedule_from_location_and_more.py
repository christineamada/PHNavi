# Generated by Django 5.1.2 on 2024-11-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0006_remove_ferryschedule_passenger_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ferryschedule',
            name='from_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ferryschedule',
            name='to_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
