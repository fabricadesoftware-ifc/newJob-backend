from rest_framework import serializers
from backend.core.models import Local


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ["cood_x", "cood_y", "street_number", "street_name", "state"]
