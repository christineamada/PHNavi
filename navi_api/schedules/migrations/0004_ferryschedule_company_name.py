# Generated by Django 5.1.2 on 2024-10-23 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_ferryschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='ferryschedule',
            name='company_name',
            field=models.CharField(default='Not specified', max_length=100),
            preserve_default=False,
        ),
    ]
