from rest_framework import serializers

from backend.core.models import User, Local
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
            "user_type",
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



class UserCompanySerializer(serializers.ModelSerializer):
    avatar_attachment_key = serializers.SlugRelatedField(
        source="avatar",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    avatar = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = User
        fields = [
            "user_type",
            "public_id",
            "name",
            "email",
            "phone",
            "cnpj",
            "fantasy_name",
            "ramo"
            "pessoa_de_contato",
            "avatar",
            "description",
            ]
        extra_kwargs = {"public_id": {"read_only": True}, "email": {"read_only": True}}


class CompanyProfileUpdateSerializer(serializers.ModelSerializer):
    # Adiciona campos para cidade e endereço
    city = serializers.CharField(write_only=True, required=False)
    street_name = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            'name',
            'avatar',
            'email',
            'phone',
            'description',
            'fantasy_name',
            'ramo',
            'city',
            'street_name',
        ]
        extra_kwargs = {
            "name": {"required": False},
            "avatar": {"required": False},
            "email": {"required": False},
            "phone": {"required": False},
            "description": {"required": False},
            "fantasy_name": {"required": False},
            "ramo": {"required": False},
            "city": {"required": False},
            "street_name": {"required": False},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError("Esse email já está em uso.")
        return value

    def update(self, instance, validated_data):
        city = validated_data.pop('city', None)
        street_name = validated_data.pop('street_name', None)

        if city and street_name:
            local, created = Local.objects.get_or_create(
                city=city,
                street_name=street_name
            )
            instance.local = local

        # Atualiza os outros campos
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance



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
            "isTravel",
            "education_level",
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
        city = validated_data.pop('city', None)

        if city:
            local, created = Local.objects.get_or_create(city=city)
            instance.local = local

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone",
        ]
