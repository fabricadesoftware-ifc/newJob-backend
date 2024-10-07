from django.db import models
from .company import Company
from .local import Local
from .benefit import Benefit
from .category import Category
from backend.files.models import Image
from django.utils import timezone


class Job(models.Model):

    class EducationLevel(models.IntegerChoices):
        FUNDAMENTAL = 1, "Ensino Fundamental",
        MEDIO = 2, "Ensino Médio",
        SUPERIOR = 3, "Ensino Superior",
        GRADUACAO = 4, "Pós-Graduação",
        MESTRADO = 5, "Mestrado",
        DOUTORADO = 6, "Doutorado"
    title = models.CharField(max_length=255)
    description = models.TextField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    deadline = models.DateField()
    isPcd = models.BooleanField(default=False)
    isTravel = models.BooleanField(default=False)
    wage = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    benefits = models.ManyToManyField(Benefit, related_name="jobs", blank=True)
    educatiol_Level = models.IntegerField(choices=EducationLevel.choices, default=EducationLevel.MEDIO)
    category = models.ForeignKey(Category, related_name="jobs", on_delete=models.PROTECT, null=True, blank=True)
    isExpired = models.BooleanField(default=False)
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
        return self.title
