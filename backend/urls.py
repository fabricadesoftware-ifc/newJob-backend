from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from backend.core.views import AuthView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from backend.core.router import router
from backend.files.router import router as router_files

from backend.core.auth.login import LoginUser
from backend.core.auth.register import RegisterUser
from backend.core.auth.reset_password import ResetPasswordUser
from backend.core.auth.forgot_password import ForgotPasswordUser

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/v1/files/", include(router_files.urls)),
    path("api/v1/accounts/", include("rest_registration.api.urls")),
    path("api/token/", AuthView.as_view(), name="token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # OpenAPI documentation
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/v1/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # Administration site
    path("api/admin/", admin.site.urls),
    path("api/login", LoginUser, name="login"),
    path("api/register", RegisterUser, name="register"),
    path("api/forgot-password", ForgotPasswordUser, name="forgot-password"),
    path("api/reset-password", ResetPasswordUser, name="reset-password"),

]

from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
