from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from ..models import User, Company 

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def ResetPasswordUser(request):
    reset_code = request.data.get("reset_code")
    new_password = request.data.get("new_password")

    if not reset_code or not new_password:
        return Response({"message": "Todos os campos são necessários."}, status=status.HTTP_400_BAD_REQUEST)

    user_or_company = None
    is_company = False

    try:
        user_or_company = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        try:
            user_or_company = Company.objects.get(id=request.user.id)
            is_company = True
        except Company.DoesNotExist:
            return Response({"message": "Usuário ou empresa não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if user_or_company.reset_code != reset_code:
        return Response({"message": "Código de redefinição inválido."}, status=status.HTTP_400_BAD_REQUEST)

    user_or_company.password = make_password(new_password)
    user_or_company.reset_code = None
    user_or_company.save()

    return Response({"message": "Senha redefinida com sucesso."}, status=status.HTTP_200_OK)
