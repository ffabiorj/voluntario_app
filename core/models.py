from django.db import models


class Acao(models.Model):
    nome_acao = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_acao


class Voluntario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    acao = models.ForeignKey(Acao, related_name="voluntarios", on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
