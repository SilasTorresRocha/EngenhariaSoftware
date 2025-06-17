from django.contrib import admin
from django.urls import path, include
from api.views import ValidarUsuarioView , CriarUsuarioView, gerar_planejamento, SincronizarProvasTrabalhosView, ConsultarProvasTrabalhosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('planner/', include('planner.urls')),
    
    path('gerar-planejamento/', gerar_planejamento),
    path('api/validarUsuario', ValidarUsuarioView.as_view()),
    path('criarUsuario', CriarUsuarioView.as_view()),
    path('sincronizar-provas-trabalhos/', SincronizarProvasTrabalhosView.as_view()),
    path('consultar-provas-trabalhos/', ConsultarProvasTrabalhosView.as_view()),
]
