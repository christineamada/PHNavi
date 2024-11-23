from django.db import models

class BusSchedule(models.Model):
    """
    Represents a bus schedule.

    Attributes:
        company_name (str): Company operating the bus.
        from_location (str): Origin location.
        from_latitude (Decimal): Latitude for the origin.
        from_longitude (Decimal): Longitude for the origin.
        to_location (str): Destination location.
        to_latitude (Decimal): Latitude for the destination.
        to_longitude (Decimal): Longitude for the destination.
        departure_time (time): Departure time.
        arrival_time (time, optional): Arrival time (nullable).
        travel_class (str): Travel class (e.g., AC, non-AC).
        fare (Decimal): Fare in PHP.
        travel_days (str): Days of operation (e.g., "1, 2, 3, 4, 5, 6, 7").
    """
    company_name = models.CharField(max_length=100)
    from_location = models.CharField(max_length=255)
    from_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    from_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    to_location = models.CharField(max_length=255)
    to_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    to_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    departure_time = models.TimeField()
    arrival_time = models.TimeField(null=True, blank=True, help_text="Format: HH:MM AM/PM")
    travel_class = models.CharField(max_length=50)
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    travel_days = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.company_name} from {self.from_location} to {self.to_location}"

  
class FerrySchedule(models.Model):
    """
    Represents a ferry schedule.

    Attributes:
        company_name (str): Company operating the ferry.
        from_location (str): Origin location.
        to_location (str): Destination location.
        vessel (str): Vessel name.
        departure_time (time): Departure time.
        day_of_departure (str): Days of departure (e.g., "1, 2, 3, 4, 5, 6, 7").
        day_of_arrival (str, optional): Days of arrival (nullable).
        accommodation (str): Type of accommodation (e.g., Economy).
        fare (Decimal): Fare in PHP.
    """
    company_name = models.CharField(max_length=100)
    from_location = models.CharField(max_length=255, null=True, blank=True)
    to_location = models.CharField(max_length=255, null=True, blank=True)
    vessel = models.CharField(max_length=100, null=True, blank=True)
    departure_time = models.TimeField(null=True, blank=True, help_text="Format: HH:MM")
    day_of_departure = models.CharField(max_length=50, null=True, blank=True)
    arrival_time = models.TimeField(null=True, blank=True, help_text="Format: HH:MM")
    day_of_arrival = models.CharField(max_length=50, null=True, blank=True)
    accommodation = models.CharField(max_length=50, null=True, blank=True)
    fare = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.vessel} from {self.from_location} to {self.to_location}"