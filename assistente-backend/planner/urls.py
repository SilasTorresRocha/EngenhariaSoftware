from django.urls import path
from .views import oi

urlpatterns = [
    path('', oi),
]
