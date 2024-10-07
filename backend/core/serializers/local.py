from rest_framework import serializers
from backend.core.models import Local
from backend.core.serializers.state import StateSerializer


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ["id", "latitude", "longitude", "street_number", "street_name", "city", "state"]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        try:
            representation['longitude'] = float(instance.longitude) if instance.longitude is not None else None
            representation['latitude'] = float(instance.latitude) if instance.latitude is not None else None
        except InvalidOperation:
            representation['longitude'] = "Valor inválido"
            representation['latitude'] = "Valor inválido"
        
        return representation


class LocalDetailSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = Local
        fields = ["id","longitude", "latitude", "street_number", "street_name", "city", "state"]
