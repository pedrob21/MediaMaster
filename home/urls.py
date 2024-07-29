from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('calcular_media/', views.calcular_media, name='calcular_media'),
]
