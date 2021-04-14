import pytest
import pprint
from django.urls import reverse
from rest_framework import status

from backend.core.models import User
from backend.core.models import Company


@pytest.mark.django_db
def test_list_company(api_client, user_factory, company_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=[])

    # DADO um tipo de contrato
    company1 = company_factory()

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para listar as empresas.
    resp = api_client.get(reverse("company-list"))

    # ENTÃO a resposta deve ser de sucesso
    assert resp.status_code == status.HTTP_200_OK

    # ENTÃO o usuário deve uma lista de empresas
    assert len(resp.data) > 0

    # E ENTÃO o primeiro elemento deve ter o 'name' do objeto previamente criado
    assert resp.data[0]["name"] == company1.name


@pytest.mark.django_db
def test_detail_company(api_client, user_factory, company_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=[])

    # DADO um tipo de contrato
    company1 = company_factory()

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para detalhar uma empresa.
    resp = api_client.get(reverse("company-detail", kwargs={"id": company1.id}))

    # ENTÃO a resposta deve ser de sucesso
    assert resp.status_code == status.HTTP_200_OK

    # E ENTÃO o campo 'name' deve ser igual ao do objeto previamente criado
    assert resp.data["name"] == company1.name

    # E ENTÃO o campo 'cnpj' deve ser igual ao do objeto previamente criado
    assert resp.data["cnpj"] == company1.cnpj


@pytest.mark.django_db
def test_detail_company_invalid(api_client, user_factory, company_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=[])

    # DADO um tipo de contrato
    company1 = company_factory()

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para detalhar uma empresa não criada.
    resp = api_client.get(reverse("company-detail", kwargs={"id": company1.id + 1}))

    # ENTÃO a resposta deve ser não encontrada (404)
    assert resp.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_list_company_invalido(api_client, company_factory):

    # DADO um tipo de contrato
    company1 = company_factory()

    # QUANDO a API é chamada para listar os empresas, sem um usuário autenticado.
    resp = api_client.get(reverse("company-list"))

    # ENTÃO a resposta deve ser de acesso não autorizado
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED