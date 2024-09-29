from rest_framework import viewsets

from backend.core.models import Category
from backend.core.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    lookup_field = "id"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
