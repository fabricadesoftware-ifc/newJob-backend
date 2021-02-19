from rest_framework.routers import DefaultRouter

from backend.files import views

app_name = "files"

router = DefaultRouter()
router.register("images", views.ImageUploadViewSet)
router.register("documents", views.DocumentUploadViewSet)