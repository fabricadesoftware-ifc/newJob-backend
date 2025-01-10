from django.db.models import Q
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from datetime import timedelta
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from ..models.user import User
from ..models.company import Company


User = get_user_model()

@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny])
def LoginUser(request):
    value = request.data.get("value")
    password = request.data.get("password")
    print("Value:", value)
    print("Password:", password)

    if value is not None and password is not None:

            user = User.objects.get(Q(username=value) | Q(email=value))
            if user and check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                access = refresh.access_token

                response_data = {
                    "refresh": str(refresh),
                    "access": str(access),
                    "username": user.username,
                    "email": user.email,
                    "id": user.id,
                    "type": user.user_type,
                    "message": "Login realizado com sucesso!"
                }
                return Response(response_data, status=status.HTTP_200_OK)
    return Response(
        {"message": "Credenciais inválidas!"},
        status=status.HTTP_400_BAD_REQUEST
    )
