from rest_framework import viewsets

from backend.core.models import ContractType
from backend.core.serializers import ContractTypeSerializer


class ContractTypeViewSet(viewsets.ModelViewSet):
    queryset = ContractType.objects.all()
    serializer_class = ContractTypeSerializer