from django.db import models
from .state import State


class Local(models.Model):
    longitude = models.BigIntegerField()
    latitude = models.BigIntegerField()
    city = models.CharField(max_length=85)
    street_number = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.longitude, self.latitude
