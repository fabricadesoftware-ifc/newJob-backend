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
            "name",
            "email",
            "phone",
            "linkedin",
            "avatar",
            "description",
            "comorbidade",
            "avatar_attachment_key",
        ]
        depth = 1
        extra_kwargs = {"public_id": {"read_only": True}, "email": {"read_only": True}}



class UserUpdateSerializer(serializers.ModelSerializer):
    city = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "phone",
            "avatar",
            "linkedin",
            "description",
            "comorbidade",
            "city",
        ]
        extra_kwargs = {
            "name": {"required": False},
            "email": {"required": False},
            "phone": {"required": False},
            "avatar": {"required": False},
            "linkedin": {"required": False},
            "description": {"required": False},
            "isPcd": {"required": False},
            "isTravel": {"required": False},
            "education_level": {"required": False},
            "comorbidade": {"required": False},
            "city": {"required": False},
        }

    def update(self, instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            # "username",
            "email",
            "phone",
        ]
        depth = 1
