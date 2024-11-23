from django.db import models

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    from_coords = models.JSONField()
    to_coords = models.JSONField()

    def __str__(self):
        return self.name