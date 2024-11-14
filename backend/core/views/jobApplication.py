from rest_framework import viewsets

from backend.core.models import JobApplication
from backend.core.serializers import JobApplicationSerializer


class JobApplicationViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    lookup_field = "id"
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
