import pytest
from django.urls import reverse
from core.models import Acao


@pytest.fixture
def create_acao():
    return Acao.objects.create(
        nome_acao="Doacoes",
        instituicao="Bradesco",
        local="Rio de Janeiro",
        descricao="Doar comida",
    )


@pytest.fixture
def payload_correto(create_acao):
    data = {
        "nome": "Fabio",
        "sobrenome": "Oliveira",
        "bairro": "Realengo",
        "cidade": "Rio de Janeiro",
        "acao": create_acao.pk,
    }
    return data


@pytest.fixture
def payload_incorreto():
    data = {
        "nome": "",
        "sobrenome": "",
        "bairro": "Realengo",
        "cidade": "Rio de Janeiro",
        "acao": 0,
    }
    return data


@pytest.mark.django_db
def test_method_post(client, payload_correto):
    url = reverse("voluntario_lista")
    response = client.post(url, data=payload_correto)
    assert response.status_code == 201


@pytest.mark.django_db
def test_method_post_dados_invalidos(client, payload_incorreto):
    url = reverse("voluntario_lista")
    response = client.post(url, data=payload_incorreto)
    assert response.status_code == 400
