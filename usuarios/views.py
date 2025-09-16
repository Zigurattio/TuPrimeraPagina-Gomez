from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login
from usuarios.forms import Registrarse as FormularioRegistro, Editar_Perfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra

def iniciar_sesion(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            
            login(request, usuario)
            
            DatosExtra.objects.get_or_create(user=usuario)
            
            return redirect('inicio')
            
    else: 
        formulario = AuthenticationForm()

    return render(request, 'usuarios/iniciar_sesion.html', {'formulario': formulario})

def registrarse(request):
    
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('iniciar_sesion')
        
    else:
        formulario = FormularioRegistro()
        
    return render(request, 'usuarios/registrarse.html', {'formulario': formulario})

@login_required
def perfil(request):
    datos_extra = request.user.datosextra 
    return render(request, 'usuarios/perfil.html', {'usuario': request.user, 'datos_extra': datos_extra})


@login_required
def editar_perfil(request):
    
    datos_extra = request.user.datosextra
    
    
    if request.method == 'POST':
        formulario = Editar_Perfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            avatar_nuevo = formulario.cleaned_data.get('avatar')
            if avatar_nuevo:
                datos_extra.avatar = avatar_nuevo
            
            datos_extra.save()
            formulario.save()
            return redirect('perfil')
    else:
         formulario =  Editar_Perfil(instance=request.user, initial={'avatar':request.user.datosextra.avatar})
    return render(request, 'usuarios/editar_perfil.html', {"formulario": formulario})
            
class EditarContraseña(PasswordChangeView): 
   template_name = "usuarios/cambiar_contraseña.html"
   success_url = reverse_lazy('perfil')
           

