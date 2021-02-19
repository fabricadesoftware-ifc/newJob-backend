from rest_framework import serializers

from backend.core.models import User
from backend.files.models import Image
from backend.files.serializers import ImageSerializer


class UserProfileSerializer(serializers.ModelSerializer):

    avatar_attachment_key = serializers.SlugRelatedField(
        source="avatar",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    avatar = ImageSerializer(required=False, read_only=True)

    def create(self, validated_data):
        raise NotImplementedError("Use UserCreateSerializer")

    class Meta:
        model = User
        fields = [
            "public_id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "linkedin",
            "profile_title",
            "profile_description",
            "avatar",
            "avatar_attachment_key",
        ]
        extra_kwargs = {"public_id": {"read_only": True}, "email": {"read_only": True}}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "phone", "linkedin", "profile_title", "profile_description"]
