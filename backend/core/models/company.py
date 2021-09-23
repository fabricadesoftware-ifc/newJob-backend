from django.db import models
from .contractType import ContractType


class Company(models.Model):
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    contract_types = models.ManyToManyField(ContractType)

    def __str__(self):
        return self.name