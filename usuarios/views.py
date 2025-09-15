from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from usuarios.models import UserData
from usuarios.forms import Register, EditProfileForm, EditPasswordForm

def login(request):
    if request.method == "POST":
        form_login = AuthenticationForm(request, data=request.POST)
        if form_login.is_valid():
            user = form_login.get_user()

            auth_login(request, user)

            UserData.objects.get_or_create(user=user)
            return redirect('inicio')
    else:
        form_login = AuthenticationForm()

    return render(request, 'usuarios/iniciar_sesion.html', {'form_login': form_login})

def register(request):

    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()

            return redirect("iniciar_sesion")
    else:
        form = Register()

    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'usuarios/perfil.html')

@login_required
def edit_profile(request):

    userdata = request.user.userdata

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():

            new_avatar = form.cleaned_data.get('avatar')
            if new_avatar:
                userdata.avatar = new_avatar
            userdata.save()
            form.save()
            return redirect('perfil')
    else:
        form = EditProfileForm(instance=request.user, initial={'avatar': request.user.userdata.avatar})

    return render(request, 'usuarios/editar_perfil.html', {'form': form})

class EditPassword(PasswordChangeView):
    template_name = 'usuarios/editar_contrasenia.html'
    form_class = EditPasswordForm  
    success_url = reverse_lazy('perfil')