from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from usuarios.forms import registrarse as FormularioRegistro

def iniciar_sesion(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            
            login(request, usuario)
            
            return redirect('pagina:inicio')
            
    else: 
        formulario = AuthenticationForm()

    return render(request, 'usuarios/iniciar_sesion.html', {'formulario': formulario})

def registrarse(request):
    
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('usuarios:iniciar_sesion')
        
    else:
        formulario = FormularioRegistro()
        
    return render(request, 'usuarios/registrarse.html', {'formulario': formulario})
            
           
