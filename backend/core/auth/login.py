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

from ..models.company import Company

def generate_company_token(company):
    # Criar um RefreshToken associado a um usuário
    refresh = RefreshToken.for_user(company)
    refresh["id"] = company.id  # Adicione dados ao payload
    refresh["email"] = company.email
    refresh["type"] = "company"  # Identifique o tipo de usuário

    access = refresh.access_token  # Gera o access token

    return str(refresh), str(access)

@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny])
def LoginUser(request):
    value = request.data.get("value")
    password = request.data.get("password")
    print("Value:", value)
    print("Password:", password)

    if value is not None and password is not None:
        # Verifica login de User
        try:
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
                    "type": "user",
                    "message": "Login realizado com sucesso!"
                }
                return Response(response_data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            pass

        # Verifica login de Company
        try:
            company = Company.objects.get(email=value)
            if company and check_password(password, company.password):
                refresh, access = generate_company_token(company)

                response_data = {
                    "refresh": refresh,
                    "access": access,
                    "name": company.name,
                    "email": company.email,
                    "id": company.id,
                    "type": "company",
                    "message": "Login realizado com sucesso!"
                }
                return Response(response_data, status=status.HTTP_200_OK)
        except Company.DoesNotExist:
            pass

    return Response(
        {"message": "Credenciais inválidas!"},
        status=status.HTTP_400_BAD_REQUEST
    )
