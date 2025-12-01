from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm

# Create your views here.
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listar.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/form_libro.html', {'form': form})

def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/form_libro.html', {'form': form})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete()
    return redirect('listar_libros')