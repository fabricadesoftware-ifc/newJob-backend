from rest_framework import viewsets

from backend.core.models import Job
from backend.core.serializers import JobSerializer
from backend.core.serializers.job import JobDetailSerializer


class JobViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    lookup_field = "id"
    queryset = Job.objects.all()
    serializer_classes = {"list": JobDetailSerializer, "retrierve": JobDetailSerializer}
    default_serializer_class = JobSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
