from django.urls import path
from .views import gerar_planejamento

urlpatterns = [
    path('gerar-planejamento/', gerar_planejamento),
]
