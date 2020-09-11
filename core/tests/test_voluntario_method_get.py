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
def test_voluntanrio_retorna_status_200(client):
    url = reverse("voluntario_lista")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_voluntario_retorna_vazio(client):
    url = reverse("voluntario_lista")
    response = client.get(url)
    assert response.data == []


@pytest.mark.django_db
def test_retorna_um_voluntario(client, create_voluntario):
    url = reverse("voluntario_lista")
    response = client.get(url)
    data = [
        {
            "nome": "Fabio",
            "sobrenome": "Oliveira",
            "bairro": "Realengo",
            "cidade": "Rio de Janeiro",
        }
    ]
    assert response.data == data


@pytest.mark.django_db
def test_obtem_voluntario_por_id_status_ok(client, create_voluntario):
    url = reverse("voluntario_detalhe", kwargs={"pk": create_voluntario.pk})
    response = client.get(
        url,
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_obtem_voluntario_por_id_errado(client, create_voluntario):
    url = reverse("voluntario_detalhe", kwargs={"pk": 5})
    response = client.get(
        url,
    )
    assert response.status_code == 404