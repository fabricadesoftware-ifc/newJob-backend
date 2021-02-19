from rest_framework import viewsets

from backend.core.models import Company
from backend.core.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer