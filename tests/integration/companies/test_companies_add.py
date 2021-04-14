import pytest
import pprint
from django.urls import reverse
from rest_framework import status

from backend.core.models import User
from backend.core.models import ContractType


@pytest.mark.django_db
def test_add_companies_nao_autorizado(api_client, user_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=[])

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para criar uma empresa válida.
    resp = api_client.post(reverse("company-list"), {"name": "Nova empresa"})

    # ENTÃO a resposta deve ser de acesso não autorizado (403)
    assert resp.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_add_company_nao_autenticado(api_client, contractType_factory):
    # QUANDO a API é chamada para criar uma empresa válido.
    resp = api_client.post(reverse("company-list"), {"name": "Nova empresa"})

    # ENTÃO a resposta deve ser de acesso não autorizado (401)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_add_contractType_valido(api_client, user_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=["core.add_company"])

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para criar uma empresa válida.
    resp = api_client.post(reverse("company-list"), {"name": "Nova empresa", "email": "email@novaempresa.com", "cnpj": "10635424000186"})

    # ENTÃO a resposta deve ser created (201)
    assert resp.status_code == status.HTTP_201_CREATED

    # E ENTÃO o item alterado deve ser devolvido
    assert resp.data["name"] == "Nova empresa"


@pytest.mark.django_db
def test_add_contractType_invalido(api_client, user_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=["core.add_company"])

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para criar uma empresa com campo faltante
    resp = api_client.post(reverse("company-list"), {"name": "Nova empresa", "email": "email@novaempresa.com"})

    # ENTÃO a resposta deve ser solicitacao inválida (400)
    assert resp.status_code == status.HTTP_400_BAD_REQUEST
