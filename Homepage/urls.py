from django.http import HttpRequest,HttpResponse,JsonResponse
from django.shortcuts import render
from django.urls import path,include
from . import views,models

urlpatterns = [
    path('',views.HomePage),
]