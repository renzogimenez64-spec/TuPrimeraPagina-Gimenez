from django.urls import path
from usuarios.views import login, register, profile, edit_profile, EditPassword
from django.contrib.auth.views import LogoutView 

urlpatterns = [

    path('iniciar-sesion/', login, name='iniciar_sesion'),
    path('registro/', register, name='registro'),
    path('perfil/', profile, name='perfil'),
    path('perfil/editar/', edit_profile, name='editar_perfil'),
    path('perfil/editar/contrasenia/', EditPassword.as_view(), name='editar_contrasenia'),
    path('cerrar-sesion/', LogoutView.as_view(template_name="usuarios/cerrar_sesion.html"), name='cerrar_sesion')
]