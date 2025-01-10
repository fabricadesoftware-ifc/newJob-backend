from backend.core.models import Company
from rest_framework import viewsets, status
from rest_framework.decorators import action
from backend.core.serializers import JobApplicationSerializer, CompanyDetailSerializer, CompanySerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed



class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
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


