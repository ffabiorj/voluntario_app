from django.db import models


class Acao(models.Model):
    nome_acao = models.CharField(max_length=100, blank=False, null=False)
    instituicao = models.CharField(max_length=100, blank=False, null=False)
    local = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.nome_acao


class Voluntario(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    sobrenome = models.CharField(max_length=100, blank=False, null=False)
    bairro = models.CharField(max_length=50, blank=False, null=False)
    cidade = models.CharField(max_length=50, blank=False, null=False)
    acao = models.ForeignKey(Acao, related_name="voluntarios", on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
