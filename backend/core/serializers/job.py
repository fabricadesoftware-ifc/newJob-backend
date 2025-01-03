from rest_framework import serializers
from backend.core.models import Job
from backend.core.serializers.company import CompanyDetailSerializer
from backend.core.serializers.local import LocalDetailSerializer
from rest_framework.pagination import PageNumberPagination
from .jobApplication import JobApplicationSerializer


class JobSerializer(serializers.ModelSerializer):
    wage = serializers.DecimalField(
        max_digits=7,
        decimal_places=2,
        required=False,
        allow_null=True
    )
    applications = JobApplicationSerializer(many=True, read_only=True)
    remaining_spots = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = "__all__"
        depth = 2

    def get_remaining_spots(self, instance):
        if instance.isClosed:
            return "Vagas acabaram"

        if instance.applications.filter(is_selected=True).exists():
            return "Vaga já foi selecionada"

        return max(0, instance.max_candidates - instance.applications.count())

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['wage'] = representation['wage'] if representation['wage'] is not None else "A Combinar"
        return representation




class JobDetailSerializer(serializers.ModelSerializer):
    company = CompanyDetailSerializer(read_only=True)
    local = LocalDetailSerializer(read_only=True)
    remaining_spots = serializers.SerializerMethodField()

    class Meta:
        model = Job
        depth = 2
        fields = ["id", "title", "description", "local", "company", "deadline", "remaining_spots"]

    def get_remaining_spots(self, instance):
        if instance.isClosed:
            return "Vagas acabaram"
        return max(0, instance.max_candidates - instance.applications.count())

    def get_remaining_spots(self, instance):
        return max(0, instance.max_candidates - instance.applications.count())


class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["title", "benefits", "wage", "education_level", "isPcd", "isTravel", "deadline"]
        
    def create(self, validated_data):
        benefits = validated_data.pop("benefits", [])
        job = Job.objects.create(**validated_data)
        job.benefits.set(benefits)
        return job




class JobPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4
