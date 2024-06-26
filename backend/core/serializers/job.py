from rest_framework import serializers
from backend.core.models import Job, ContractType
from backend.core.serializers.company import CompanyDetailSerializer
from backend.core.serializers.local import LocalDetailSerializer


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["id", "title", "description", "local", "company", "deadline"]


class JobDetailSerializer(serializers.ModelSerializer):

    company = CompanyDetailSerializer(read_only=True)
    local = LocalDetailSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ["id", "title", "description", "local", "company", "deadline"]
