from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from ..models.user import User
from ..serializers.user import UserUpdateSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def UpdateCompany(request):
    user = request.user


    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def UpdateUser(request):
    user = request.user

    if user.user_type != User.UserType.STANDARD:
        return Response(
            {"detail": "Apenas usuários do tipo 'Usuário padrão' podem atualizar o perfil."},
            status=status.HTTP_403_FORBIDDEN
        )

    serializer = UserUpdateSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
