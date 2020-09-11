import pytest
from core.models import Acao, Voluntario
from django.urls import reverse


@pytest.fixture
def create_acao():
    return Acao.objects.create(
        nome_acao="Doacoes",
        instituicao="Bradesco",
        local="Rio de Janeiro",
        descricao="Doar comida",
    )


@pytest.fixture
def create_voluntario(create_acao):
    return Voluntario.objects.create(
        nome="Fabio",
        sobrenome="Oliveira",
        bairro="Realengo",
        cidade="Rio de Janeiro",
        acao=create_acao,
    )


@pytest.mark.django_db
def test_acao_retorna_status_200(client):
    url = reverse("acao_lista")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_acao_retorna_vazio(client):
    url = reverse("acao_lista")
    response = client.get(url)
    assert response.data == []


@pytest.mark.django_db
def test_retorna_uma_acao(client, create_acao, create_voluntario):
    url = reverse("acao_lista")
    response = client.get(url)
    data = [
        {
            "nome_acao": "Doacoes",
            "instituicao": "Bradesco",
            "local": "Rio de Janeiro",
            "descricao": "Doar comida",
            "voluntarios": ["Fabio"],
        }
    ]
    assert response.data == data


@pytest.mark.django_db
def test_obtem_acao_por_id_status_ok(client, create_voluntario, create_acao):
    url = reverse("acao_detalhe", kwargs={"pk": create_acao.pk})
    response = client.get(
        url,
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_obtem_acao_por_id_errado(client, create_voluntario, create_acao):
    url = reverse("acao_detalhe", kwargs={"pk": 5})
    response = client.get(
        url,
    )
    assert response.status_code == 404
