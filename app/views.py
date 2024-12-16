from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'app/inicio.html')

def acerca_de(request):
    return render(request, 'app/acerca_de.html')

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:listado_clientes')
    else:
        form = ClienteForm()
    return render(request, 'app/crear_cliente.html', {'form': form})

def listado_clientes(request):
    busqueda = request.GET.get('busqueda_clientes')
    if busqueda:
        lista_clientes = Cliente.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(apellido__icontains=busqueda) |
            Q(email__icontains=busqueda))
    else:
        lista_clientes = Cliente.objects.all()

    return render(request, 'app/listado_clientes.html', {'listado_clientes': lista_clientes})

@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('app:listado_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'app/editar_cliente.html', {'form': form, 'cliente': cliente})

@login_required
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('app:listado_clientes')
    return render(request, 'app/eliminar_cliente.html', {'cliente': cliente})