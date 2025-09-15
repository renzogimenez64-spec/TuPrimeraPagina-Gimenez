from django import forms

class CrearLibro(forms.Form):
    nombre = forms.CharField(max_length=50)
    portada = forms.ImageField(required=False)
    autor = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=50)
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