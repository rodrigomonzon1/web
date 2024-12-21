from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioListView, UsuarioDetailView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView, registro, perfil, editar_perfil, CambiarContraseña, mensajeria

app_name = 'usuarios'

urlpatterns = [
    path('usuario_list/', UsuarioListView.as_view(), name='usuario-list'),
    path('<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    path('nuevo/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('<int:pk>/eliminar/', UsuarioDeleteView.as_view(), name='usuario-delete'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registro/', registro, name = 'registro'),
    path('perfil/', perfil, name = 'perfil'),
    path('perfil/editar/', editar_perfil, name = 'editar_perfil'),
    path('perfil/cambiar_contraseña/', CambiarContraseña.as_view(), name = 'cambiar_contraseña'),
    path('mensajeria/', mensajeria, name='mensajeria')
]
