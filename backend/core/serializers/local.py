from rest_framework import serializers
from backend.core.models import Local


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ["longitude", "latitude", "street_number", "street_name", "state"]
