from django.db.models import Q
from django.contrib.auth import authenticate, get_user_model
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth.hashers import make_password

from ..models.user import User
from ..models.company import Company

User = get_user_model()

@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny])
def RegisterUser(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if not username or not email or not password:
        return Response(
            {"message": "Dados de usuário inválidos!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {"message": "Usuário já existe"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(email=email).exists():
        return Response(
            {"message": "Email já existe"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create(username=username, email=email)
    user.set_password(password)
    user.save()

    response_data = {
        "message": "Usuário criado com sucesso!",
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }
    return Response(response_data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny])
def RegisterCompany(request):
    name = request.data.get("name")
    fantasy_name = request.data.get("fantasy_name")
    email = request.data.get("email")
    cnpj = request.data.get("cnpj")
    telefone = request.data.get("telefone")
    password = request.data.get("password")

    if not all([name, fantasy_name, email, cnpj, telefone, password]):
        return Response(
            {"message": "Todos os campos são obrigatórios!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if Company.objects.filter(cnpj=cnpj).exists() or Company.objects.filter(email=email).exists():
        return Response(
            {"message": "CNPJ ou email já cadastrado!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    hashed_password = make_password(password)

    company = Company.objects.create(
        name=name,
        fantasy_name=fantasy_name,
        email=email,
        cnpj=cnpj,
        telefone=telefone,
        password=hashed_password
    )
    company.save()

    response_data = {
        "message": "Empresa criada com sucesso!",
        "id": company.id,
        "name": company.name,
        "fantasy_name": company.fantasy_name,
        "email": company.email,
        "cnpj": company.cnpj,
        "telefone": company.telefone,
    }
    return Response(response_data, status=status.HTTP_201_CREATED)
