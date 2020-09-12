import pytest
from core.models import Acao, Voluntario


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
def test_criar_acao(create_acao):
    assert Acao.objects.count() == 1


@pytest.mark.django_db
def test_str_acao(create_acao):
    assert create_acao.__str__() == "Doacoes"


@pytest.mark.django_db
def test_criar_voluntario(create_voluntario):
    assert Voluntario.objects.count() == 1


@pytest.mark.django_db
def test_str_voluntario(create_voluntario):
    assert create_voluntario.__str__() == "Fabio"
