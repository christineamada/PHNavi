from rest_framework import serializers
from .models import BusSchedule, FerrySchedule

class BusScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusSchedule
        fields = '__all__'

class FerryScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FerrySchedule
        fields = '__all__'