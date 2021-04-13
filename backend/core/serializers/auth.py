from rest_framework import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from backend.core.models import User


class AuthSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        data["username"] = self.user.username
        data["email"] = self.user.email
        data["name"] = self.user.name
        data["public_id"] = self.user.public_id

        return data
