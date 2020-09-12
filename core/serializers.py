from rest_framework import serializers
from core.models import Voluntario, Acao


class VoluntarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voluntario
        fields = ["nome", "sobrenome", "bairro", "cidade", "acao"]


class AcaoSerializer(serializers.ModelSerializer):
    voluntarios = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Acao
        fields = ["nome_acao", "instituicao", "local", "descricao", "voluntarios"]
