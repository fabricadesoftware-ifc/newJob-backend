from backend.core.models import Company
from rest_framework import viewsets, status
from rest_framework.decorators import action
from backend.core.serializers import JobApplicationSerializer, CompanyDetailSerializer, CompanySerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed




class IsCompanyUser(BasePermission):
    """
    Permissão que verifica se o usuário autenticado é uma Company.
    """
    def has_permission(self, request, view):
        user = request.user
        if user and hasattr(user, 'is_authenticated') and user.is_authenticated:
            # Aqui vamos verificar se o tipo do usuário no token é "company"
            print(f"User authenticated: {user.username} (type: {request.auth.get('type')})")
            if request.auth.get("type") == "company":
                return True  # Se for uma "company", permite o acesso
        return False  # Se não for "company", negamos o acesso

class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsCompanyUser]
    lookup_field = "id"
    queryset = Company.objects.all()
    serializer_classes = {
        "list": CompanyDetailSerializer,
        "retrieve": CompanyDetailSerializer,
    }
    default_serializer_class = CompanySerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=False, methods=["get"], url_path='my-jobs')
    def getMyJobs(self, request):
        company = request.user
        jobs = company.job_set.all()
        serializer = JobApplicationSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


