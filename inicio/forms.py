from django import forms
from .models import Libro

class CrearLibro(forms.Form):
    nombre = forms.CharField(max_length=50)
    portada = forms.ImageField(required=False)
    autor = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=80)
    descripcion = forms.CharField(       
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        required=False                   
    )
    fecha_de_publicacion = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'  
            }
        ),) 

class ActualizarLibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = "__all__"  
        widgets = {
            'fecha_de_publicacion': forms.DateInput(attrs={'type': 'date'})
        }