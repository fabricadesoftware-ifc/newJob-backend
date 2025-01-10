from rest_framework.response import Response
from ..models.job import Job
from ..serializers.job import JobSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from backend.core.models import Job
from backend.core.serializers.jobApplication import JobApplicationSerializer
from rest_framework import status

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def getJobs(request):
    if request.user.is_authenticated and request.user.user_type == 'COMPANY':
        jobs = Job.objects.filter(company=request.user)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    else:
        return Response({"detail": "Não autorizado."}, status=403)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_job_applications(request, job_id):
    """Obter as applications de um trabalho específico"""

    if not request.user.is_authenticated:
        return Response({"detail": "Não autorizado."}, status=status.HTTP_403_FORBIDDEN)

    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return Response({"detail": "Job não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.user != job.company:
        return Response({"detail": "Você não tem permissão para ver as applications deste trabalho."}, status=status.HTTP_403_FORBIDDEN)

    applications = job.applications.all()  # Supondo que 'applications' é um campo relacionado

    serializer = JobApplicationSerializer(applications, many=True)

    return Response(serializer.data)
