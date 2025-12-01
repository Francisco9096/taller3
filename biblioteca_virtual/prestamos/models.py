from django.db import models
from libros.models import Libro

# Create your models here.

class Prestamo(models.Model):
    usuario = models.CharField(max_length=100)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.libro.titulo}"