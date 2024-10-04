from rest_framework import serializers
from backend.core.models import Job
from backend.core.serializers.company import CompanyDetailSerializer
from backend.core.serializers.local import LocalDetailSerializer
from rest_framework.pagination import PageNumberPagination


class JobSerializer(serializers.ModelSerializer):
    wage_display = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = "__all__"

    def get_wage_display(self, obj):
        return obj.wage if obj.wage is not None else "A Combinar"


class JobDetailSerializer(serializers.ModelSerializer):
    company = CompanyDetailSerializer(read_only=True)
    local = LocalDetailSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ["id", "title", "description", "local", "company", "deadline"]


class JobPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4
