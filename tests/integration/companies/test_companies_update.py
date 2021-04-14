import pytest
import pprint
from django.urls import reverse
from rest_framework import status

from backend.core.models import User
from backend.core.models import ContractType


@pytest.mark.django_db
def test_update_company_nao_autorizado(api_client, user_factory, company_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=[])

    # DADO uma empresa
    company1 = company_factory()

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para atualizar um tipo de contrato válido.
    resp = api_client.patch(reverse("company-detail", kwargs={"id": company1.id}), {"name": "novaEmpresa"})

    # ENTÃO a resposta deve ser de acesso não autorizado (403)
    assert resp.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_update_company_nao_autenticado(api_client, company_factory):
    # DADO um tipo de contrato
    company1 = company_factory()

    # QUANDO a API é chamada para alterar um tipo de contrato válido.
    resp = api_client.patch(reverse("company-detail", kwargs={"id": company1.id}), {"name": "novaEmpresa"})

    # ENTÃO a resposta deve ser de acesso não autorizado (401)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_update_company_valido(api_client, user_factory, company_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=["core.change_company"])

    # DADO um tipo de contrato
    company1 = company_factory()

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para alterar um tipo de contrato válido.
    resp = api_client.patch(reverse("company-detail", kwargs={"id": company1.id}), {"name": "novaEmpresa"})

    # ENTÃO a resposta deve ser ok (200)
    assert resp.status_code == status.HTTP_200_OK

    # E ENTÃO o item alterado deve ser devolvido
    assert resp.data["name"] == "novaEmpresa"


@pytest.mark.django_db
def test_update_company_invalido(api_client, user_factory, company_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=["core.change_company"])

    # DADO um tipo de contrato
    company1 = company_factory()

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para alterar um tipo de contrato com id inválido
    resp = api_client.patch(reverse("company-detail", kwargs={"id": company1.id + 1}), {"name": "novaEmpresa"})

    # ENTÃO a resposta deve ser item não encontrado (404)
    assert resp.status_code == status.HTTP_404_NOT_FOUND
