from django.urls import path
from .views import BusScheduleListCreate, FerryScheduleListCreate

urlpatterns = [
    path('bus-schedules/', BusScheduleListCreate.as_view(), name='bus-schedule-list-create'),
    path('ferry-schedules/', FerryScheduleListCreate.as_view(), name='ferry-schedule-list-create'),
]