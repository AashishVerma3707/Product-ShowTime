from django.db import models
from django.contrib.auth.models import User
import requests
# Create your models here.


class Movies(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}-{self.id}"


class Booking(models.Model):
    booked_by=models.ForeignKey(User, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movies, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.booked_by.username}_{self.movie.title}"


