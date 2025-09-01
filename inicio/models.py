from django.db import models

class Libro(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    fecha_de_publicacion = models.DateField(auto_now_add=True)
