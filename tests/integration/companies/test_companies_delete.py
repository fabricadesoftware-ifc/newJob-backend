import pytest
import pprint
from django.urls import reverse
from rest_framework import status

from backend.core.models import User
from backend.core.models import Company


@pytest.mark.django_db
def test_delete_company_nao_autorizado(api_client, user_factory, company_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=[])

    # DADO uma empresa
    company1 = company_factory()

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para excluir uma empresa válido.
    resp = api_client.delete(reverse("company-detail", kwargs={"id": company1.id}))

    # ENTÃO a resposta deve ser de acesso não autorizado (403)
    assert resp.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_delete_company_nao_autenticado(api_client, company_factory):
    # DADO uma empresa
    company1 = company_factory()

    # QUANDO a API é chamada para excluir uma empresa válido.
    resp = api_client.delete(reverse("company-detail", kwargs={"id": company1.id}))

    # ENTÃO a resposta deve ser de acesso não autorizado (401)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_delete_company_valido(api_client, user_factory, company_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=["core.delete_company"])

    # DADO uma empresa
    company1 = company_factory()

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para excluir uma empresa válido.
    resp = api_client.delete(reverse("company-detail", kwargs={"id": company1.id}))

    # ENTÃO a resposta deve ser item excluido sem conteúdo (204)
    assert resp.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_delete_company_invalido(api_client, user_factory, company_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=["core.delete_company"])

    # DADO uma empresa
    company1 = company_factory()

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para excluir uma empresa com id inválido
    resp = api_client.delete(reverse("company-detail", kwargs={"id": company1.id + 1}))

    # ENTÃO a resposta deve ser item não encontrado (404)
    assert resp.status_code == status.HTTP_404_NOT_FOUND
