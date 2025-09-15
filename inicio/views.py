from django.shortcuts import render, redirect 
from inicio.models import Libro
from inicio.forms import CrearLibro
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'inicio/index.html') 

@login_required
def crear_libro(request):
    if request.method == "POST":
        print(request.POST)
        formulario = CrearLibro(request.POST, request.FILES)
        if formulario.is_valid():
            nombre_nuevo = formulario.cleaned_data.get('nombre')
            autor_nuevo = formulario.cleaned_data.get('autor')
            genero_nuevo = formulario.cleaned_data.get('genero')
            fecha_nueva = formulario.cleaned_data.get('fecha')
            nueva_descripcion = formulario.cleaned_data.get('descripcion')
            nueva_portada = formulario.cleaned_data.get('portada')
            

            libro = Libro(nombre=nombre_nuevo, autor=autor_nuevo, genero=genero_nuevo, descripcion=nueva_descripcion, fecha_de_publicacion=fecha_nueva, portada=nueva_portada,)
            libro.save()

            return redirect('lista_libros')
    else:   
        formulario = CrearLibro()
    return render(request, 'inicio/crear_libro.html', {'formulario': formulario})

def lista_libros(request):
    libros = Libro.objects.all()  
    return render(request, 'inicio/lista_libros.html', {'lista_libros': libros})

def detalle_libro(request, libro_id):

    libro = Libro.objects.get(id=libro_id)

    return render(request, 'inicio/detalle_libro.html', {'libro': libro})

# def actualizar_libro(request, libro_id)

class ActualizarLibro(LoginRequiredMixin, UpdateView):

    model = Libro
    template_name = "inicio/actualizar_libro.html"
    fields = "__all__"
    success_url = reverse_lazy('lista_libros')
     
class EliminarLibro(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "inicio/eliminar_libro.html"
    success_url = reverse_lazy('lista_libros') 