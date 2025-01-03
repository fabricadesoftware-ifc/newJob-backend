from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from backend.core.models import User, Job, JobApplication
from backend.core.serializers import UserProfileSerializer, UserUpdateSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_classes = {
        "list": UserProfileSerializer,
        "retrieve": UserProfileSerializer,
        "update": UserUpdateSerializer,
        "partial_update": UserUpdateSerializer,
    }
    default_serializer_class = UserProfileSerializer
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Retorna o usuário autenticado"""
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def accept_vacancy(self, request, pk=None):
        """Permite que o usuário se candidate a uma vaga especificada pelo job_id"""
        job = get_object_or_404(Job, id=pk)
        print(job)

        if job.isClosed:
            return Response(
                {"error": "Essa vaga está fechada para novas candidaturas"},
                status=status.HTTP_400_BAD_REQUEST
            )

        job.check_max_candidates()
        if job.isClosed:
            return Response(
                {"error": "Essa vaga está fechada para novas candidaturas"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if JobApplication.objects.filter(user=request.user, job=job).exists():
            return Response(
                {"error": "Você já se candidatou para essa vaga"},
                status=status.HTTP_400_BAD_REQUEST
            )

        JobApplication.objects.create(user=request.user, job=job, status=JobApplication.StatusJob.PENDENTE)

        return Response(
            {"message": "Candidatura realizada com sucesso"},
            status=status.HTTP_201_CREATED
        )

    @action(detail=False, methods=["patch", "put"], permission_classes=[IsAuthenticated])
    def atualizar_perfil(self, request):
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK) 
