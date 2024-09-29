from rest_framework import serializers
from backend.core.models.benefit import Benefit


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = "__all__"