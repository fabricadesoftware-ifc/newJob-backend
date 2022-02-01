from rest_framework import serializers
from backend.core.models import Job, ContractType
from backend.core.serializers.company import CompanyDetailSerializer
from backend.core.serializers.contractType import ContractTypeSerializer
from backend.core.serializers.local import LocalSerializer


class JobSerializer(serializers.ModelSerializer):

    contract_types = ContractTypeSerializer(read_only=True, many=True)
    company = CompanyDetailSerializer(read_only=True)
    local = LocalSerializer(read_only=True)
 
    class Meta:
        model = Job
        fields = ["id", "title", "description", "local", "contract_types", "company", "deadline"]
