from rest_framework import viewsets

from backend.core.models import UserJob
from backend.core.serializers import UserJobSerializer


class UserJobViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = UserJob.objects.all()
    serializer_class = UserJobSerializer
