from rest_framework import serializers
from backend.core.models import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ["id", "name", "initials"]