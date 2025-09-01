from django.shortcuts import render, redirect 
from inicio.models import Libro
from inicio.forms import CrearLibro

def inicio(request):
    return render(request, 'inicio/index.html') 

def crear_libro(request):

    if request.method == "POST":
        print(request.POST)
        formulario = CrearLibro(request.POST)
        if formulario.is_valid():
            nombre_nuevo = formulario.cleaned_data.get('nombre')
            autor_nuevo = formulario.cleaned_data.get('autor')
            genero_nuevo = formulario.cleaned_data.get('genero')
            fecha_nueva = formulario.cleaned_data.get('genero')
            

            libro = Libro(nombre=nombre_nuevo, autor=autor_nuevo, genero=genero_nuevo, fecha_de_publicacion=fecha_nueva,)
            libro.save()

            return redirect('inicio')
    else:   
        formulario = CrearLibro()
    return render(request, 'inicio/crear_libro.html', {'formulario': formulario})

def lista_libros(request):
    libros = Libro.objects.all()  
    return render(request, 'inicio/lista_libros.html', {'libros_libros': libros})