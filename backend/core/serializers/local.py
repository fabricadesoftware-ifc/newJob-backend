from rest_framework import serializers
from backend.core.models import Local
from backend.core.serializers.state import StateSerializer


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ["longitude", "latitude", "street_number", "street_name", "city", "state"]


class LocalDetailSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = Local
        fields = ["longitude", "latitude", "street_number", "street_name", "city", "state"]
