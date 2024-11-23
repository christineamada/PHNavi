# schedules/admin.py
from django.contrib import admin
from .models import BusSchedule, FerrySchedule

@admin.register(BusSchedule)
class BusScheduleAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'from_location', 'to_location', 'departure_time', 'arrival_time', 'travel_class', 'fare')
    search_fields = ('company_name', 'from_location', 'to_location')

@admin.register(FerrySchedule)
class FerryScheduleAdmin(admin.ModelAdmin):
    list_display = ('from_location', 'to_location', 'vessel', 'departure_time', 'accommodation', 'fare')
    search_fields = ('from_location', 'to_location', 'vessel')