from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from backend.core.models import Job

class Command(BaseCommand):
    help = "Deleta jobs expirados há mais de duas semanas"

    def handle(self, *args, **kwargs):
        expiration_date = timezone.now().date() - timedelta(weeks=2)
        Job.objects.filter(isExpired=True, deadline__lt=expiration_date).delete()
        self.stdout.write(self.style.SUCCESS('Jobs expirados há mais de duas semanas foram deletados com sucesso.'))
