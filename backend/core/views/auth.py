from rest_framework_simplejwt.views import TokenObtainPairView

from backend.core.serializers import AuthSerializer
from backend.core.models import User


class AuthView(TokenObtainPairView):
    serializer_class = AuthSerializer
