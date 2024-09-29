from rest_framework.routers import DefaultRouter

from backend.core import views

router = DefaultRouter()

router.register(r"companies", views.CompanyViewSet, basename="company")
router.register(r"job", views.JobViewSet, basename="job")
router.register(r"local", views.LocalViewSet, basename="local")
router.register(r"state", views.StateViewSet, basename="state")
router.register(r"user_job", views.UserJobViewSet, basename="user_job")
router.register(r"categories", views.CategoryViewSet, basename="categories")
router.register(r"benefits", views.BenefitViewSet, basename="benefits")
