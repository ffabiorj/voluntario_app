from django.urls import path
from core import views as view

urlpatterns = [
    path("voluntario/", view.VoluntarioLista.as_view(), name="voluntario_lista"),
    path(
        "voluntario/<int:pk>/",
        view.VoluntarioDetalhe.as_view(),
        name="voluntario_detalhe",
    ),
    path("acao/", view.AcaoLista.as_view(), name="acao_lista"),
    path("acao/<int:pk>/", view.AcaoDetalhe.as_view(), name="acao_detalhe"),
]