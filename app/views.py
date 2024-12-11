from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente
from django.db.models import Q


def inicio(request):
    return render(request, 'app/inicio.html')

def acerca_de(request):
    return render(request, 'app/acerca_de.html')

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:inicio')
    else:
        form = ClienteForm()
    return render(request, 'app/crear_cliente.html', {'form': form})

def listado_clientes(request):
    busqueda = request.GET.get('busqueda_clientes')
    if busqueda:
        listado_clientes = Cliente.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(apellido__icontains=busqueda) |
            Q(email__icontains=busqueda))
    else:
        listado_clientes = Cliente.objects.all()

    return render(request, 'app/listado_clientes.html', {'listado_clientes': listado_clientes})
