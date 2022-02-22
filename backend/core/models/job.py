from django.db import models
from .company import Company
from .local import Local


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    deadline = models.DateField()

    def __str__(self):
        return self.title
