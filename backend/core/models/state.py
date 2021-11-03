from django.db import models


class State(models.Model):
    name = models.CharField(max_length=255)
    initials = models.CharField(max_length=2)

    def __str__(self):
        return self.initials
