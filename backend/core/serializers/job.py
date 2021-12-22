from rest_framework import serializers
from backend.core.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["id", "title", "description", "local", "contract_types", "company", "deadline"]
