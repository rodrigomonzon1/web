from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Usuario, InfoUsuario, Mensaje
from .forms import UsuarioForm, RegistroDeUsuario, EditarPerfil, MensajeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect


class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'

class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'usuarios/usuario_detail.html'
    context_object_name = 'usuario'

class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuarios:usuario-list')

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuarios:usuario-list')

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuarios:usuario-list')
    
def registro(request):
    formulario = RegistroDeUsuario()
    
    if request.method == "POST":
        formulario = RegistroDeUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
    
    return render(request, 'usuarios/registro.html', {'form': formulario})

def perfil(request):
    
    return render(request, 'usuarios/perfil.html', {})

from django.core.exceptions import ObjectDoesNotExist

@login_required
def editar_perfil(request):
    info_usuario, created = InfoUsuario.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user, info_usuario_instance=info_usuario)
        if formulario.is_valid():
            formulario.save()  # Guarda los datos de User e InfoUsuario
            return redirect('usuarios:perfil')
        else:
            print("Errores del formulario:", formulario.errors)  # Depuración de errores
    else:
        formulario = EditarPerfil(instance=request.user, info_usuario_instance=info_usuario)

    return render(request, 'usuarios/editar_perfil.html', {'form': formulario})




class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_contraseña.html'
    success_url = reverse_lazy('usuarios:perfil')
    
@login_required
def mensajeria(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.usuario = request.user  # Asigna el usuario autenticado
            mensaje.save()
            return redirect('usuarios:mensajeria')
    else:
        form = MensajeForm()

    mensajes = Mensaje.objects.all().order_by('-fecha_creacion')
    return render(request, 'usuarios/mensajeria.html', {'form': form, 'mensajes': mensajes})

