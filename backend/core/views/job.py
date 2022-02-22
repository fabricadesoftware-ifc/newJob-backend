from rest_framework import viewsets

from backend.core.models import Job
from backend.core.serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    # lookup_field = "id"
    queryset = Job.objects.all()
    serializer_class = JobSerializer
