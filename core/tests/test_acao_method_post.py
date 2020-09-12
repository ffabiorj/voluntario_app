import pytest
from django.urls import reverse


@pytest.fixture
def dados_acao():
    data = {
        "nome_acao": "Doacoes",
        "instituicao": "Bradesco",
        "local": "Rio de Janeiro",
        "descricao": "Doar comida",
    }
    return data


@pytest.fixture
def dados_errados():
    data = {"nome_acao": "", "instituicao": 1, "local": 1, "descricao": 1}
    return data


@pytest.mark.django_db
def test_status_code_201(client, dados_acao):
    url = reverse("acao_lista")
    response = client.post(url, data=dados_acao)
    assert response.status_code == 201


@pytest.mark.django_db
def test_status_code_400(client, dados_errados):
    url = reverse("acao_lista")
    response = client.post(url, data=dados_errados)
    assert response.status_code == 400
