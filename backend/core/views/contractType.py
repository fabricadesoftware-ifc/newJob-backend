from rest_framework import viewsets

from backend.core.models import ContractType
from backend.core.serializers import ContractTypeSerializer


class ContractTypeViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    lookup_field = "id"
    queryset = ContractType.objects.all()
    serializer_class = ContractTypeSerializer
    http_method_names = ["get", "delete", "patch", "post"]
