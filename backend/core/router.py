from rest_framework.routers import DefaultRouter

from backend.core import views

router = DefaultRouter()

router.register(r"companies", views.CompanyViewSet, basename="company")
router.register(r"contract_types", views.CompanyViewSet, basename="contract_type")