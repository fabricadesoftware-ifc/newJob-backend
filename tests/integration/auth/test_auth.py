import pytest
from django.urls import reverse
from rest_framework import status

from backend.core.models import User


@pytest.mark.django_db
def test_user_login(api_client, user_factory):
    # DADO dados válidos para um usuário.
    existing_user = user_factory(name="user_a", permissions=[])

    # QUANDO a API é chamada para autenticar o usuário.
    resp = api_client.post(reverse("token"), {"username": "user_a@example.com", "password": "user_a"})

    # ENTÃO a resposta de sucesso deve conter os dados do usuário.
    assert resp.status_code == status.HTTP_200_OK

    # ENTÃO o usuário deve receber os itens:
    #  'public_id', 'access', 'refresh', 'username', 'email', 'name'
    assert str(resp.data["public_id"]) == str(existing_user.public_id)
    assert resp.data["access"] != ""
    assert resp.data["refresh"] != ""
    assert resp.data["username"] == "user_a@example.com"
    assert resp.data["email"] == "user_a@example.com"


@pytest.mark.django_db
def test_user_invalid_login(api_client, user_factory):
    # DADO dados válidos para um usuário.
    existing_user = user_factory(name="user_a", permissions=[])

    # QUANDO a API é chamada para autenticar o usuário com a senha inválida.
    resp = api_client.post(reverse("token"), {"username": "user_a@example.com", "password": "user_b"})

    # ENTÃO a resposta de sucesso deve conter os dados do usuário.
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


# @pytest.mark.django_db
# def test_retrieve_current_valid(api_client, user_factory):
#     # DADO um user autenticado.
#     user = user_factory(name="user", permissions=[])
#     api_client.force_authenticate(user=user)

#     # QUANDO a API é chamada para obter o user atual.
#     resp = api_client.get(reverse("user-current"))

#     # ENTÃO a resposta deve ser de sucesso.
#     assert resp.status_code == status.HTTP_200_OK


# @pytest.mark.django_db
# def test_retrieve_current_invalid(api_client, user_factory):
#     # DADO nenhum user autenticado.

#     # QUANDO a API é chamada para obter o user atual.
#     resp = api_client.get(reverse("user-current"))

#     # ENTÃO a resposta deve ser falta de permissão
#     assert resp.status_code == status.HTTP_401_UNAUTHORIZED


# @pytest.mark.django_db
# def test_update_current_valid(api_client, user_factory):
#     # DADO um use2r autenticado.
#     user = user_factory(name="user", permissions=[])
#     api_client.force_authenticate(user=user)

#     # QUANDO a API é chamada para editar o user atual.
#     resp = api_client.put(
#         reverse("user-current"),
#         {"first_name": "New first name", "last_name": "New last name", "email": "user@example.com",},
#     )
#     # ENTÃO a resposta de sucesso deve conter o user modificado.
#     assert resp.status_code == status.HTTP_200_OK
#     assert resp.data["first_name"] == "New first name"

#     # E ENTÃO o user deve ser modificado no banco.
#     assert User.objects.get(pk=user.pk).first_name == "New first name"


# @pytest.mark.django_db
# def test_update_current_invalid(api_client):
#     # DADO nenhum user autenticado.

#     # QUANDO a API é chamada para editar o user atual.
#     resp = api_client.put(reverse("user-current"), {"first_name": "New first name", "last_name": "New last name"},)

#     # ENTÃO a resposta deve ser falta de permissão
#     assert resp.status_code == status.HTTP_401_UNAUTHORIZED


# @pytest.mark.django_db
# def test_delete_current_valid(api_client, user_factory):
#     # DADO um user autenticado.
#     user = user_factory(name="user", permissions=[])
#     api_client.force_authenticate(user=user)

#     # QUANDO a API é chamada para remover o user atual.
#     resp = api_client.delete(reverse("user-current"))

#     # ENTÃO a resposta deve ser de sucesso.
#     assert resp.status_code == status.HTTP_204_NO_CONTENT

#     # E ENTÃO o user deve ser removido do banco.
#     assert User.objects.filter(pk=user.pk).exists() is False


# @pytest.mark.django_db
# def test_delete_current_invalid(api_client):
#     # DADO nenhum user autenticado.

#     # QUANDO a API é chamada para remover o user atual.
#     resp = api_client.delete(reverse("user-current"))

#     # ENTÃO a resposta deve ser falta de permissão
#     assert resp.status_code == status.HTTP_401_UNAUTHORIZED
