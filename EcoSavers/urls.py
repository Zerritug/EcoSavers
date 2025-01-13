from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('HomePage/', include('Homepage.urls')),
    path('Educacion/', include('Educacion.urls')),
    path('Empresas/', include('Empresas.urls')),
    path('PaginaDeInicio/', include('PaginaInicial.urls')),
]