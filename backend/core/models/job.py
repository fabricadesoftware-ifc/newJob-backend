from django.db import models
from .benefit import Benefit
from .category import Category
from backend.files.models import Image
from django.utils import timezone
from .user import User
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
    deadline = models.DateField()
    isPcd = models.BooleanField(default=False)
    isTravel = models.BooleanField(default=False)
    wage = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    benefits = models.ManyToManyField(Benefit, related_name="jobs", blank=True)
    education_level = models.IntegerField(choices=EducationLevel.choices, default=EducationLevel.MEDIO)
    max_candidates = models.PositiveIntegerField(default=1)
    ramo = models.ForeignKey(Category, related_name="jobs", on_delete=models.PROTECT, null=True, blank=True)
    isExpired = models.BooleanField(default=False)
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    isClosed = models.BooleanField(default=False)
    image_job = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    selected_user = models.ForeignKey(
        User,
        related_name="selected_jobs",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def check_expiration(self):
        if self.deadline < timezone.now().date():
            self.isExpired = True
            self.isClosed = True
            self.save()
        else:
            self.isExpired = False
            self.save()

    def check_max_candidates(self):
        if self.applications.count() >= self.max_candidates:
            self.isClosed = True
            self.save()

    def __str__(self):
        return self.title
