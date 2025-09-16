from django.shortcuts import render, redirect
from django.http import HttpResponse
from pagina.models import Cigarro
from pagina.forms import FormularioCreacionCigarro
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render(request, 'inicio/inicio.html') 

@login_required
def crear_cigarro(request):
    
    if request.method == 'POST':
        print(request.POST)
        formulario = FormularioCreacionCigarro(request.POST, request.FILES)
        if formulario.is_valid():
            marca_nueva = formulario.cleaned_data.get('marca')
            cantidad_nueva = formulario.cleaned_data.get('cantidad')
            imagen_nueva = formulario.cleaned_data.get('imagen')
            
            cigarro = Cigarro(marca=marca_nueva, cantidad=cantidad_nueva, imagen=imagen_nueva)
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


class ActualizarCigarro(LoginRequiredMixin, UpdateView):
    model = Cigarro
    template_name = "inicio/actualizar_cigarro.html"
    fields = "__all__"
    success_url = reverse_lazy('listado_de_cigarros')
    
    
class EliminarCigarro(LoginRequiredMixin,DeleteView):
    model = Cigarro
    template_name = "inicio/eliminar_cigarro.html"
    success_url = reverse_lazy("listado_de_cigarros")


    