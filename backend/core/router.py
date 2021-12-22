from rest_framework.routers import DefaultRouter

from backend.core import views

router = DefaultRouter()

router.register(r"companies", views.CompanyViewSet, basename="company")
router.register(r"contract_types", views.ContractTypeViewSet, basename="contract_type")
router.register(r"job", views.JobViewSet, basename="job")
router.register(r"contract_types", views.LocalViewSet, basename="local")
router.register(r"contract_types", views.StateViewSet, basename="state")
router.register(r"contract_types", views.UserJobViewSet, basename="user_job")
