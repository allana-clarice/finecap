"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from finecap.views import adicionar_reserva,excluir_reserva,detalhes_reserva,lista_reservas,index

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),
    path('adicionar/', adicionar_reserva, name='adicionar_reserva'),
    path('listar', lista_reservas, name='lista_reservas'),
    path('detalhe/<int:id>/', detalhes_reserva, name='detalhes_reserva'),
    path('excluir_reserva/<int:id>/', excluir_reserva, name='exluir_reserva'),
]
