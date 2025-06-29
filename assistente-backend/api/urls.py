from django.urls import path
from .views import gerar_planejamento
from .views import ValidarUsuarioView
from .views import CriarUsuarioView, ValidarUsuarioView, gerar_planejamento, SincronizarProvasTrabalhosView, ConsultarProvasTrabalhosView, consultar_planejamento


urlpatterns = [
    path('gerar-planejamento/', gerar_planejamento),
    path('validarUsuario/', ValidarUsuarioView.as_view()), #endpoint fornecedifo pelo frontend (so obedeci kkkk)
    path('criarUsuario/', CriarUsuarioView.as_view()),
    path('sincronizar-provas-trabalhos/', SincronizarProvasTrabalhosView.as_view()),
    path('consultar-provas-trabalhos/', ConsultarProvasTrabalhosView.as_view()),
    path('consultar-planejamento/', consultar_planejamento),
]
