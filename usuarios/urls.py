from django.urls import path
from usuarios.views import login
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('iniciar-sesion/', login, name='iniciar_sesion'),
    path('cerrar-sesion/', LogoutView.as_view(template_name="usuarios/cerrar_sesion.html"), name='cerrar_sesion')
]