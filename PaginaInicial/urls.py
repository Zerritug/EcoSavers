from django.urls import path
from . import views

urlpatterns = [
    path('', views.Pag , name='PaginaDeInicio'),
]