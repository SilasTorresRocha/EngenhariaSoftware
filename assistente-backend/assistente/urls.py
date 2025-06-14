from django.contrib import admin
from django.urls import path, include
from api.views import ValidarUsuarioView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('planner/', include('planner.urls')),
    path('api/validarUsuario', ValidarUsuarioView.as_view()),
]
