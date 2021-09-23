from rest_framework import serializers

from backend.core.models import Company
from .contractType import ContractTypeSerializer


class CompanySerializer(serializers.ModelSerializer):
    contract_types = ContractTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ["id", "name", "email", "cnpj", "contract_types"]


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "cnpj"]
