from django.urls import path 
from inicio.views import inicio, crear_libro, lista_libros, detalle_libro, ActualizarLibro

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear-libro/', crear_libro, name='crear_libro'),
    path('libro/', lista_libros, name='lista_libros'),
    path('libro/<libro_id>/', detalle_libro, name='detalle_libro'),
    path('libro/<pk>/actualziacion/', ActualizarLibro.as_view(), name='actualizar_libro'),
]
