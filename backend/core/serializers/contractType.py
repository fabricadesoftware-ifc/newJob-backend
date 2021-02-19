from rest_framework import serializers

from backend.core.models import ContractType


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractType
        fields = ["id", "description"]