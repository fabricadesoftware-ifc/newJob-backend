from django.db import models
from .contractType import ContractType
from .company import Company
from .local import Local


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=14, unique=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    contract_types = models.ManyToManyField(ContractType)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    deadline = models.DateField()

    def __str__(self):
        return self.title