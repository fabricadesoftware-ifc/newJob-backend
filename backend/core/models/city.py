from django.db import models
from .state import State


class City(models.Model):
    name = models.CharField(max_length=100)
    state_city = models.ForeignKey(
        State,
        related_name= "state_city",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return (f"{self.name}, {self.state_city}")

