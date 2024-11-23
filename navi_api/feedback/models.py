from django.db import models


class Feedback(models.Model):
    RATING_CHOICES = [
        ('Excellent', 'Excellent'),
        ('Very Good', 'Very Good'),
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Poor', 'Poor'),
    ]


    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    rating = models.CharField(max_length=20, choices=RATING_CHOICES)


    def __str__(self):
        return self.name