from django.db import models
from django.utils import timezone

class Libro(models.Model):
    portada = models.ImageField(upload_to='portadas_libros', null=True)
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=80)
    descripcion = models.TextField(blank=True, null=True)
    fecha_de_publicacion = models.DateField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return f"Titulo: {self.nombre} Autor: {self.autor} Generos: {self.genero} Descripcion: {self.descripcion} Fecha De Publicacion: {self.fecha_de_publicacion}"