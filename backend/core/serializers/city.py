from rest_framework import serializers
from backend.core.models.city import City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "name", "state_city"]
