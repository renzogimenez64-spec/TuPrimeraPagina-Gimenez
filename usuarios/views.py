from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def login(request):
    if request.method == "POST":
        form_login = AuthenticationForm(request, data=request.POST)
        if form_login.is_valid():
            user = form_login.get_user()

            login(request, user)

            return redirect('inicio')
    else:
        form_login = AuthenticationForm()

    return render(request, 'usuarios/iniciar_sesion.html', {'form_login': form_login})