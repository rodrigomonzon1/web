from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('listado_clientes/', views.listado_clientes, name='listado_clientes'),
    path('editar_cliente/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
]
