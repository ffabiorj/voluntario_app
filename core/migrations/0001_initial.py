# Generated by Django 3.1.1 on 2020-09-11 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Acao",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_acao", models.CharField(max_length=100)),
                ("instituicao", models.CharField(max_length=100)),
                ("local", models.CharField(max_length=100)),
                ("descricao", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Voluntario",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("sobrenome", models.CharField(max_length=100)),
                ("bairro", models.CharField(max_length=50)),
                ("cidade", models.CharField(max_length=50)),
                (
                    "acao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="voluntarios",
                        to="core.acao",
                    ),
                ),
            ],
        ),
    ]