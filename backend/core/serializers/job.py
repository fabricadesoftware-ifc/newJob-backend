from rest_framework import serializers
from backend.core.models import Job
from backend.core.serializers.company import CompanyDetailSerializer
from backend.core.serializers.local import LocalDetailSerializer
from rest_framework.pagination import PageNumberPagination
from .jobApplication import JobApplicationSerializer
from .company import CompanyDetailSerializer


class JobSerializer(serializers.ModelSerializer):
    wage = serializers.DecimalField(
        max_digits=8,
        decimal_places=2,
        required=False,
        allow_null=True
    )
    company = CompanyDetailSerializer(read_only=True)
    applications = JobApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = "__all__"
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['wage'] = representation['wage'] if representation['wage'] is not None else "A Combinar"
        return representation


class JobDetailSerializer(serializers.ModelSerializer):
    company = CompanyDetailSerializer(read_only=True)

    class Meta:
        model = Job
        depth = 2
        fields = ["id", "title", "description", "cityState", "company", "deadline"]


class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["title", "benefits", "wage", "contract_type", "isTravel", "deadline"]

    def create(self, validated_data):
        benefits = validated_data.pop("benefits", [])
        job = Job.objects.create(**validated_data)
        job.benefits.set(benefits)
        return job

class JobPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4
