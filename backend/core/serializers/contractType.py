from rest_framework import serializers

from backend.core.models import ContractType


class ContractTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractType
        fields = ["id", "description"]
