from django import forms 

class FormularioCreacionCigarro(forms.Form):
    marca = forms.CharField(max_length=20)
    cantidad = forms.CharField(max_length=20)