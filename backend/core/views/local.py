from rest_framework import viewsets

from backend.core.models import Local
from backend.core.serializers import LocalSerializer


class LocalViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    lookup_field = "id"
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
