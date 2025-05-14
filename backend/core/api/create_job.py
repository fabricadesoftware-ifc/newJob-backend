from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from ..models.job import Job
from ..models.benefit import Benefit
from ..models.category import Category
from backend.files.models import Image

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create_job(request):
    user = request.user

    title = request.data.get("title")
    description = request.data.get("description")
    deadline = request.data.get("deadline")
    isPcd = request.data.get("isPcd", False)
    isTravel = request.data.get("isTravel", False)
    wage = request.data.get("wage")
    education_level = request.data.get("education_level", Job.ContractType.ESTAGIARIO)
    max_candidates = request.data.get("max_candidates", 1)
    ramo_id = request.data.get("ramo")
    benefits_ids = request.data.get("benefits", [])
    # image_job_id = request.data.get("image_job")

    if not title or not description or not deadline:
        return Response(
            {"error": "Os campos obrigatórios (title, description, deadline) não foram preenchidos."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    ramo = None
    if ramo_id:
        try:
            ramo = Category.objects.get(id=ramo_id)
        except Category.DoesNotExist:
            return Response({"error": "A categoria especificada não existe."}, status=status.HTTP_400_BAD_REQUEST)

    benefits = []
    if benefits_ids:
        benefits = Benefit.objects.filter(id__in=benefits_ids)
        if not benefits.exists():
            return Response({"error": "Um ou mais benefícios especificados não existem."}, status=status.HTTP_400_BAD_REQUEST)

    # image_job = None
    # if image_job_id:
    #     try:
    #         image_job = Image.objects.get(id=image_job_id)
    #     except Image.DoesNotExist:
    #         return Response({"error": "A imagem especificada não existe."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        job = Job.objects.create(
            title=title,
            description=description,
            deadline=deadline,
            isPcd=isPcd,
            isTravel=isTravel,
            wage=wage,
            education_level=education_level,
            max_candidates=max_candidates,
            ramo=ramo,
            company=user,
            # image_job=image_job,
        )

        if benefits:
            job.benefits.set(benefits)

        return Response(
            {"message": "Job criado com sucesso!", "job_id": job.id},
            status=status.HTTP_201_CREATED,
        )
    except Exception as e:
        return Response(
            {"error": f"Erro ao criar o Job: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
