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
def test_method_delete_status_code_204(client, create_voluntario):
    url = reverse("voluntario_detalhe", kwargs={"pk": create_voluntario.pk})
    response = client.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_method_delete_id_errado(client, create_voluntario):
    url = reverse("voluntario_detalhe", kwargs={"pk": 5})
    response = client.delete(url)
    assert response.status_code == 404
