from django.db import models
from .job import Job
from .user import User


class JobApplication(models.Model):
    class StatusJob(models.IntegerChoices):
        PENDENTE = 1, "Pendente"
        REJEITADO = 2, "Rejeitado"
        SELECIONADO = 3, "Selecionado"
        NÃO_SELECIONADO = 4, "Não selecionado"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    status = models.IntegerField(choices=StatusJob.choices, default=StatusJob.PENDENTE)
    application_date = models.DateTimeField(auto_now_add=True)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.job.title} - {self.get_status_display()}"
