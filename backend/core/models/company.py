from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.name