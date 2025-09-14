from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Register(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        help_text=""  
    )
    password2 = forms.CharField(
        label="Repetir Contraseña",
        widget=forms.PasswordInput,
        help_text=""
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {llave: '' for llave in fields}