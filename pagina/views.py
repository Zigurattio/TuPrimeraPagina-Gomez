from django.shortcuts import render, redirect
from django.http import HttpResponse
from pagina.models import Cigarro
from pagina.forms import FormularioCreacionCigarro

def inicio(request):
    return render(request, 'inicio/inicio.html') 


def crear_cigarro(request):
    
    if request.method == 'POST':
        print(request.POST)
        formulario = FormularioCreacionCigarro(request.POST)
        if formulario.is_valid():
            marca_nueva = formulario.cleaned_data.get('marca')
            cantidad_nueva = formulario.cleaned_data.get('cantidad')
            
            cigarro = Cigarro(marca=marca_nueva, cantidad=cantidad_nueva)
            cigarro.save()
            
            return redirect('listado_de_cigarros')
            
    else:
        formulario = FormularioCreacionCigarro() 
    
    
    
    return render(request,'inicio/crear_cigarro.html', {'formulario': formulario})

def listado_cigarros(request):
    
    cigarros = Cigarro.objects.all()
    
    return render(request, 'inicio/listado_cigarros.html',{'listado_de_cigarros' : cigarros})


def detalle_cigarro(request, cigarro_id):
    
    
    cigarro = Cigarro.objects.get(id=cigarro_id)
    
    return render (request, 'inicio/detalle_cigarro.html', {'cigarro': cigarro}) 