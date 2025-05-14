from rest_framework import viewsets

from backend.core.models.city import City
from backend.core.serializers.city import CitySerializer

class CityViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    lookup_field = "id"
    queryset = City.objects.all()
    serializer_class = CitySerializer

