from django import forms 

class FormularioCreacionCigarro(forms.Form):
    marca = forms.CharField(max_length=20)
    cantidad = forms.CharField(max_length=20)
    imagen = forms.ImageField(required=False)