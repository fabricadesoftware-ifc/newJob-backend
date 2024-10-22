from rest_framework import serializers
from backend.core.models import Job
from backend.core.serializers.company import CompanyDetailSerializer
from backend.core.serializers.local import LocalDetailSerializer
from rest_framework.pagination import PageNumberPagination


class JobSerializer(serializers.ModelSerializer):
    wage = serializers.DecimalField(
        max_digits=7, 
        decimal_places=2, 
        required=False, 
        allow_null=True
    )

    class Meta:
        model = Job
        fields = "__all__"
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['wage'] = representation['wage'] if representation['wage'] is not None else "A Combinar"

        return representation


class JobDetailSerializer(serializers.ModelSerializer):
    company = CompanyDetailSerializer(read_only=True)
    local = LocalDetailSerializer(read_only=True)

    class Meta:
        model = Job
        depth = 1
        fields = ["id", "title", "description", "local", "company", "deadline"]


class JobPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4
