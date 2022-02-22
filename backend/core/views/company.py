from rest_framework import viewsets

from backend.core.models import Company
from backend.core.serializers import CompanySerializer, CompanyDetailSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    lookup_field = "id"
    queryset = Company.objects.all()
    serializer_classes = {
        "list": CompanyDetailSerializer,
        "retrieve": CompanyDetailSerializer,
    }
    default_serializer_class = CompanySerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
