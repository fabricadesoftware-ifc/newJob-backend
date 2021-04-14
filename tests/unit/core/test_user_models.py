import pytest
from backend.core.models import User


@pytest.mark.django_db
def test_user_create():
    # QUANDO criar um usuário
    User.objects.create_user("admin", "admin@admin.com", "adminpassword")
    # ENTÃO esse usuário será criado
    assert User.objects.count() == 1
    # E ENTÃO o seu username será igual ao email
    assert User.objects.get(pk=1).username == "admin@admin.com"
