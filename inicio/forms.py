from django import forms

class CrearLibro(forms.Form):
    nombre = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=50)
    fecha_de_publicacion = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'  # fuerza que sea un input con calendario
            }
        ),) 