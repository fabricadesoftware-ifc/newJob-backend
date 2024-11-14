from rest_framework import serializers
from backend.core.models import JobApplication
from backend.core.models import User
from backend.core.models import Job
from .user import UserDetailsSerializer

class JobApplicationSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_display")
    user = UserDetailsSerializer(read_only=True)
    
    class Meta:
        model = JobApplication
        fields = ["user", "application_date", "status"]
        depth = 1
