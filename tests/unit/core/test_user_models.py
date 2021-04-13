import pytest
from backend.core.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user("admin", "admin@admin.com", "adminpassword")
    assert User.objects.count() == 1
