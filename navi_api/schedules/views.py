from rest_framework import generics
from .models import BusSchedule, FerrySchedule
from .serializers import BusScheduleSerializer, FerryScheduleSerializer

# List and Create Bus Schedules
class BusScheduleListCreate(generics.ListCreateAPIView):
    queryset = BusSchedule.objects.all()
    serializer_class = BusScheduleSerializer

# List and Create Ferry Schedules
class FerryScheduleListCreate(generics.ListCreateAPIView):
    queryset = FerrySchedule.objects.all()
    serializer_class = FerryScheduleSerializer