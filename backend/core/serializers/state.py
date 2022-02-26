from rest_framework import serializers
from backend.core.models.state import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ["id", "name", "initials"]