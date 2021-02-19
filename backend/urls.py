from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from backend.core.router import router
from backend.files.router import router as router_files


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/v1/files/", include(router_files.urls)),
    path("api/v1/accounts/", include("rest_registration.api.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # OpenAPI documentation
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/swagger",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/v1/redoc",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # Administration site
    path("api/admin/", admin.site.urls),
]

from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
