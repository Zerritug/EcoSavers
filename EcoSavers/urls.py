from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('HomePage/', include('Homepage.urls')),
    path('Educacion/', include('Educacion.urls')),
    path('Prueba/', include('Prueba.urls')),
    path('PaginaDeInicio/', include('PaginaInicial.urls')),
]