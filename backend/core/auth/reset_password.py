from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from ..models.user import User

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def ResetPasswordUser(request):
    reset_code = request.data.get("reset_code")
    new_password = request.data.get("new_password")

    if not reset_code or not new_password:
        return Response({"message": "Todos os campos são necessários."}, status=status.HTTP_400_BAD_REQUEST)

    user = request.user  

    if user.reset_code != reset_code:
        return Response({"message": "Código de redefinição inválido."}, status=status.HTTP_400_BAD_REQUEST)

    user.password = make_password(new_password)
    user.reset_code = None 
    user.save()

    return Response({"message": "Senha redefinida com sucesso."}, status=status.HTTP_200_OK)