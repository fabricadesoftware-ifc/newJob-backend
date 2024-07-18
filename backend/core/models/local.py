from django.db import models
from .state import State


class Local(models.Model):
    longitude = models.DecimalField(decimal_places=2, max_digits=9)
    latitude = models.DecimalField(decimal_places=2, max_digits=9)
    city = models.CharField(max_length=85)
    street_number = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.longitude}, {self.latitude}"
