import pytest
from django.contrib.auth.models import Permission
from rest_framework.test import APIClient
from model_bakery import baker

from backend.core.models import User, ContractType


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture
def user_factory():
    def _factory(*, name, permissions):
        user = User.objects.create(email="{0}@example.com".format(name))
        user.set_password(name)
        user.save()

        for permission in permissions:
            app_label, codename = permission.split(".")
            user.user_permissions.add(Permission.objects.get(content_type__app_label=app_label, codename=codename))
        return user

    return _factory


@pytest.fixture
def contractType_factory():
    def _factory(*, description):
        contractType = ContractType.objects.create(description=description)
        contractType.save()

        return contractType

    return _factory