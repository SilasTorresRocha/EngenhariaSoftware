from django.urls import path
from .views import gerar_planejamento
from .views import ValidarUsuarioView

urlpatterns = [
    path('gerar-planejamento/', gerar_planejamento),
    path('api/validarUsuario', ValidarUsuarioView.as_view()),
]
