import pytest
from core.models import Acao, Voluntario
from django.urls import reverse
import json


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


@pytest.fixture
def payload_correto():
    data = {
        "nome_acao": "Comida",
        "instituicao": "Caixa",
        "local": "Rio de Janeiro",
        "descricao": "Doar comida",
    }
    return data


@pytest.fixture
def payload_incorreto():
    data = {"nome_acao": "", "instituicao": 1, "local": 1, "descricao": 1}
    return data


@pytest.mark.django_db
def test_method_put_status_ok(client, create_acao, payload_correto):
    url = reverse("acao_detalhe", kwargs={"pk": create_acao.pk})
    response = client.put(
        url, data=json.dumps(payload_correto), content_type="application/json"
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_method_put_status_404(client, payload_correto):
    url = reverse("acao_detalhe", kwargs={"pk": 5})
    response = client.put(
        url, data=json.dumps(payload_correto), content_type="application/json"
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_method_put_status_400(client, create_acao, payload_incorreto):
    url = reverse("acao_detalhe", kwargs={"pk": create_acao.pk})
    response = client.put(
        url, data=json.dumps(payload_incorreto), content_type="application/json"
    )
    assert response.status_code == 400
