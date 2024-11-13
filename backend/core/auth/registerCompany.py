from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from ..models.company import Company  

@api_view(["POST"])
@authentication_classes([]) 
@permission_classes([AllowAny])  
def register_company(request):
    nome = request.data.get("nome")
    nome_fantasia = request.data.get("nome_fantasia")
    email = request.data.get("email")
    telefone = request.data.get("telefone")
    endereco = request.data.get("endereco")
    cidade = request.data.get("cidade")
    password = request.data.get("password")

    if not nome or not nome_fantasia or not email or not password:
        return Response(
            {"message": "Nome, nome fantasia, email e senha são obrigatórios!"}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    if Company.objects.filter(email=email).exists():
        return Response(
            {"message": "Uma empresa com este email já existe"}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    if Company.objects.filter(nome_fantasia=nome_fantasia).exists():
        return Response(
            {"message": "Uma empresa com este nome fantasia já existe"}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    company = Company.objects.create(
        nome=nome,
        nome_fantasia=nome_fantasia,
        email=email,
        telefone=telefone,
        endereco=endereco,
        cidade=cidade,
    )
    company.set_password(password)  
    company.save()

    response_data = {
        "message": "Empresa cadastrada com sucesso!",
        "company_id": company.id,
        "nome": company.nome,
        "nome_fantasia": company.nome_fantasia,
        "email": company.email,
        "telefone": company.telefone,
        "endereco": company.endereco,
        "cidade": company.cidade,
    }
    return Response(response_data, status=status.HTTP_201_CREATED)
