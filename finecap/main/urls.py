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
from finecap.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name="index"),
    path('adicionar/', adicionar_reserva, name='adicionar_reserva'),
    path('listar/', listar_reservas, name='listar_reservas'),
    path('editar/<int:reserva_id>/', editar_reserva, name='editar_reserva'),
    path('excluir/<int:reserva_id>/', excluir_reserva, name='excluir_reserva'),
    path('reserva/<int:reserva_id>/', detalhes_reserva, name='detalhes_reserva'),
]

