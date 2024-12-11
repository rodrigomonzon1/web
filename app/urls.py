from django.urls import path
from app.views import inicio, crear_cliente, acerca_de, listado_clientes

app_name = 'app'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('acerca_de/', acerca_de, name='acerca_de'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
    path('listado_clientes/', listado_clientes, name='listado_clientes')
]
