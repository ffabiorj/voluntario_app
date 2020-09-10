from rest_framework import serializers
from core.models import Voluntario, Acoes


class VoluntarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voluntario
        exclude = []


class AcoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acoes
        exclude = []