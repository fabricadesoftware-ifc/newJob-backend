from django.db import models
from .state import State


class Local(models.Model):
    cood_x = models.CharField(max_length=255)
    cood_y = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.cood_x, self.cood_y
