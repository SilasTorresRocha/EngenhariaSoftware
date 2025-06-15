from django.urls import path
from .views import gerar_planejamento
from .views import ValidarUsuarioView
from .views import CriarUsuarioView, ValidarUsuarioView, gerar_planejamento

urlpatterns = [
    path('gerar-planejamento/', gerar_planejamento),
    path('api/validarUsuario', ValidarUsuarioView.as_view()),
    path('criarUsuario', CriarUsuarioView.as_view()),
]
