from django.urls import path
from usuarios.views import login, register
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('iniciar-sesion/', login, name='iniciar_sesion'),
    path('registro/', register, name='registro'),
    path('cerrar-sesion/', LogoutView.as_view(template_name="usuarios/cerrar_sesion.html"), name='cerrar_sesion')
]