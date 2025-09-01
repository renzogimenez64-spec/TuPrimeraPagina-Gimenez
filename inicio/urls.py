from django.urls import path 
from inicio.views import inicio, crear_libro, lista_libros

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear-libro/', crear_libro, name='crear_libro'),
    path('libro/', lista_libros, name='lista_libros'),
]
