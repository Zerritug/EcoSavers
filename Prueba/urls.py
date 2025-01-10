from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioprueba, name='Prueba'),
]