from django.db import models
from .benefit import Benefit
from .state import State
from .company import Company
from .city import City
from backend.files.models import Image
from django.utils import timezone
class Job(models.Model):
    class ContractType(models.IntegerChoices):
        CLT = 1, "CLT",
        ESTAGIARIO = 2, "Estagiário",
        PJ = 3, "PJ",
        FREELANCER = 4, "Freelancer"
    title = models.CharField(max_length=80)
    contract_type = models.IntegerField(choices=ContractType.choices, default=ContractType.ESTAGIARIO)
    state = models.ForeignKey(
        State,
        related_name="state",
        on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        City,
        related_name="city",
        on_delete=models.CASCADE
    )
    address =  models.CharField(max_length=80, null=True, blank=True)
    summary = models.TextField(max_length=200, null=True, blank=True)
    details = models.TextField(max_length=5000, null=True, blank=True)
    start = models.DateField(null=True, blank=True)
    deadline = models.DateField()
    isTravel = models.BooleanField(default=False)
    wage = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    benefits = models.ManyToManyField(Benefit, related_name="benefits", blank=True)
    isExpired = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    image_job = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def check_expiration(self):
        if self.deadline < timezone.now().date():
            self.isExpired = True
            self.save()
        else:
            self.isExpired = False
            self.save()

    def __str__(self):
        return (f"{self.title} - {self.company}")
