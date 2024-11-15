from django.db import models
from .state import State


class Local(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=4)
    longitude = models.DecimalField(max_digits=9, decimal_places=4)
    city = models.CharField(max_length=85)
    street_number = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.longitude}, {self.latitude}"

    def clean(self):
        super().clean()

        if self.longitude < -180.0 or self.longitude > 180.0:
            raise ValidationError(f"Longitude {self.longitude} deve estar entre -180 e 180.")

        if self.latitude < -90.0 or self.latitude > 90.0:
            raise ValidationError(f"Latitude {self.latitude} deve estar entre -90 e 90.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
