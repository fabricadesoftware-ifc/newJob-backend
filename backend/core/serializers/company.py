from rest_framework import serializers

from backend.core.models import Company
from .contractType import ContractTypeSerializer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "email", "cnpj"]


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "cnpj"]
