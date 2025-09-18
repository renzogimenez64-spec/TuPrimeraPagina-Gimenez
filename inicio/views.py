from django.shortcuts import render, redirect 
from inicio.models import Libro
from inicio.forms import CrearLibro, ActualizarLibroForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'inicio/index.html') 

def about(request):
    return render(request, 'inicio/about.html') 

@login_required
def crear_libro(request):
    if request.method == "POST":
        formulario = CrearLibro(request.POST, request.FILES)
        if formulario.is_valid():
            nombre_nuevo = formulario.cleaned_data.get('nombre')
            portada_nueva = formulario.cleaned_data.get('portada')
            autor_nuevo = formulario.cleaned_data.get('autor')
            genero_nuevo = formulario.cleaned_data.get('genero')
            descripcion_nueva = formulario.cleaned_data.get('descripcion')
            fecha_nueva = formulario.cleaned_data.get('fecha_de_publicacion')  

            Libro.objects.create(
                nombre=nombre_nuevo,
                portada=portada_nueva,
                autor=autor_nuevo,
                genero=genero_nuevo,
                descripcion=descripcion_nueva,
                fecha_de_publicacion=fecha_nueva   
            )

            return redirect('lista_libros')
    else:
        form = CrearLibro()

    return render(request, "inicio/crear_libro.html", {"form": form})

def lista_libros(request):
    libros = Libro.objects.all()  
    return render(request, 'inicio/lista_libros.html', {'lista_libros': libros})

def detalle_libro(request, libro_id):

    libro = Libro.objects.get(id=libro_id)

    return render(request, 'inicio/detalle_libro.html', {'libro': libro})

class ActualizarLibro(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = ActualizarLibroForm
    template_name = "inicio/actualizar_libro.html"
    success_url = reverse_lazy('lista_libros')
     
class EliminarLibro(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "inicio/eliminar_libro.html"
    success_url = reverse_lazy('lista_libros') 