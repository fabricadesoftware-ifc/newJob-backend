from rest_framework import viewsets

from backend.core.models import Benefit
from backend.core.serializers import BenefitSerializer


class BenefitViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    lookup_field = "id"
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
