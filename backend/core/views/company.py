from rest_framework import viewsets, status
from backend.core.models import Company
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from backend.core.models import JobApplication, Job
from backend.core.serializers import JobApplicationSerializer, CompanyDetailSerializer, CompanySerializer
from django.core.mail import send_mail
from django.template.loader import render_to_string


class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    lookup_field = "id"
    queryset = Company.objects.all()
    serializer_classes = {
        "list": CompanyDetailSerializer,
        "retrieve": CompanyDetailSerializer,
    }
    default_serializer_class = CompanySerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def select_candidate(self, request, pk=None):
        """
        Permite que a empresa selecione um candidato para uma vaga e remove outros candidatos da vaga.
        """
        application = self.get_object()

        job = application.job
        if job.company != request.user.company:
            return Response(
                {"error": "Você não tem permissão para escolher um candidato para essa vaga."},
                status=status.HTTP_403_FORBIDDEN
            )

        if application.is_selected:
            return Response(
                {"error": "Este candidato já foi selecionado."},
                status=status.HTTP_400_BAD_REQUEST
            )

        job.applications.filter(is_selected=True).update(is_selected=False, status=JobApplication.StatusJob.NÃO_SELECIONADO)

        application.is_selected = True
        application.status = JobApplication.StatusJob.SELECIONADO 
        application.save()

        job.selected_user = application.user
        job.save()

        subject = 'Candidato Selecionado'
        from_email = 'gabriellima2803@gmail.com' 
        to_email = [application.user.email]  

        html_content = render_to_string('../templates/html-email/vacancy_selected.html', { 'user': application.user })

        send_mail(
            subject,
            '',
            from_email,
            to_email,
            fail_silently=False,
            html_message=html_content,
        )

        if job.max_candidates == job.applications.filter(is_selected=True).count():
            job.isClosed = True  
            job.save()

        return Response(
            {"message": "Candidato selecionado com sucesso e outros candidatos removidos."},
            status=status.HTTP_200_OK
        )