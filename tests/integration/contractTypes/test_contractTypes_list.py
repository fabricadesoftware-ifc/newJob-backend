import pytest
import pprint
from django.urls import reverse
from rest_framework import status

from backend.core.models import User
from backend.core.models import ContractType


@pytest.mark.django_db
def test_list_contractType(api_client, user_factory, contractType_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=[])

    # DADO um tipo de contrato
    contractType1 = contractType_factory(description="clt")

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para listar os tipos de contrato.
    resp = api_client.get(reverse("contract_type-list"))

    # ENTÃO a resposta deve ser de sucesso
    assert resp.status_code == status.HTTP_200_OK

    # ENTÃO o usuário deve uma lista de tipos de contrato
    assert len(resp.data) > 0

    # E ENTÃO o primeiro elemento deve ter a descrição do objeto previamente criado
    assert resp.data[0]["description"] == contractType1.description


@pytest.mark.django_db
def test_list_contractType_invalido(api_client, contractType_factory):

    # DADO um tipo de contrato
    contractType1 = contractType_factory(description="clt")

    # QUANDO a API é chamada para listar os tipos de contrato, sem um usuário autenticado.
    resp = api_client.get(reverse("contract_type-list"))

    # ENTÃO a resposta deve ser de acesso não autorizado
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED