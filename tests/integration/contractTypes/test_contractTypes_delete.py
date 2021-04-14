import pytest
import pprint
from django.urls import reverse
from rest_framework import status

from backend.core.models import User
from backend.core.models import ContractType


@pytest.mark.django_db
def test_delete_contractType_nao_autorizado(api_client, user_factory, contractType_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=[])

    # DADO um tipo de contrato
    contractType1 = contractType_factory(description="clt")

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para excluir um tipo de contrato válido.
    resp = api_client.delete(reverse("contract_type-detail", kwargs={"id": contractType1.id}))

    # ENTÃO a resposta deve ser de acesso não autorizado (403)
    assert resp.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_delete_contractType_nao_autenticado(api_client, contractType_factory):
    # DADO um tipo de contrato
    contractType1 = contractType_factory(description="clt")

    # QUANDO a API é chamada para excluir um tipo de contrato válido.
    resp = api_client.delete(reverse("contract_type-detail", kwargs={"id": contractType1.id}))

    # ENTÃO a resposta deve ser de acesso não autorizado (401)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_delete_contractType_valido(api_client, user_factory, contractType_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=["core.delete_contracttype"])

    # DADO um tipo de contrato
    contractType1 = contractType_factory(description="clt")

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para excluir um tipo de contrato válido.
    resp = api_client.delete(reverse("contract_type-detail", kwargs={"id": contractType1.id}))

    # ENTÃO a resposta deve ser item excluido sem conteúdo (204)
    assert resp.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_delete_contractType_invalido(api_client, user_factory, contractType_factory):
    # DADO um usuário
    user = user_factory(name="user", permissions=["core.delete_contracttype"])

    # DADO um tipo de contrato
    contractType1 = contractType_factory(description="clt")

    # DADO que um usuario devidamente autenticado
    api_client.force_authenticate(user=user)

    # QUANDO a API é chamada para excluir um tipo de contrato com id inválido
    resp = api_client.delete(reverse("contract_type-detail", kwargs={"id": contractType1.id + 1}))

    # ENTÃO a resposta deve ser item não encontrado (404)
    assert resp.status_code == status.HTTP_404_NOT_FOUND
