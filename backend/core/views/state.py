from rest_framework import viewsets

from backend.core.models import State
from backend.core.serializers import StateSerializer


class StateViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    lookup_field = "id"
    queryset = State.objects.all()
    serializer_class = StateSerializer
