from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from backend.core.models import JobApplication, Job
from backend.core.serializers import JobSerializer
from backend.core.serializers.job import JobDetailSerializer, JobPagination


class JobViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    lookup_field = "id"
    queryset = Job.objects.all()
    serializer_classes = {"list": JobSerializer, "retrieve": JobSerializer}
    default_serializer_class = JobSerializer
    pagination_class = JobPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        for job in queryset:
            job.check_expiration()
            job.check_max_candidates()
        return queryset

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
    
    @action(detail=True, methods=["post"])
    def select_candidate(self, request, id=None):
        """
        Permite que a empresa selecione um candidato para uma vaga e remove outros candidatos da vaga.
        """
        job = get_object_or_404(Job, id=id)
        # if job.company != request.user.company:
        #     return Response(
        #         {"error": "Você não tem permissão para gerenciar candidatos dessa vaga."},
        #         status=status.HTTP_403_FORBIDDEN
        #     )

        application_id = request.data.get("application_id")
        if not application_id:
            return Response(
                {"error": "O ID do candidato é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            application = job.applications.get(id=application_id)
        except JobApplication.DoesNotExist:
            return Response(
                {"error": "Aplicação não encontrada para essa vaga."},
                status=status.HTTP_404_NOT_FOUND
            )

        if application.is_selected:
            return Response(
                {"error": "Este candidato já foi selecionado."},
                status=status.HTTP_400_BAD_REQUEST
            )

        job.applications.exclude(id=application_id).update(
            is_selected=False, status=JobApplication.StatusJob.REJEITADO
        )
        application.is_selected = True
        application.status = JobApplication.StatusJob.SELECIONADO
        application.save()

        job.selected_user = application.user
        job.save()

        subject = 'Candidato Selecionado'
        from_email = 'gabriellima2803@gmail.com'
        to_email = [application.user.email]
        html_content = render_to_string('../templates/html-email/vacancy_selected.html', {'user': application.user})
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

