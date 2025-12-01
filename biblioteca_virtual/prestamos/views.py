
from django.shortcuts import render, redirect, get_object_or_404
from .models import Prestamo
from .forms import PrestamoForm

# Create your views here.

def listar_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamos/listar.html', {'prestamos': prestamos})

def crear_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_prestamos')
    else:
        form = PrestamoForm()
    return render(request, 'prestamos/form_prestamo.html', {'form': form})

def editar_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, id=id)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('listar_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'prestamos/form_prestamo.html', {'form': form})

def eliminar_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, id=id)
    prestamo.delete()
    return redirect('listar_prestamos')