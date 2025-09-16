from django.urls import path
from usuarios.views import iniciar_sesion, registrarse, perfil, editar_perfil, EditarContraseña
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', LogoutView.as_view(template_name="usuarios/cerrar_sesion.html"), name='cerrar_sesion'),
    path('registrarse/', registrarse, name='registrarse'),
    path('perfil', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/editar/cambiar_contraseña', EditarContraseña.as_view(), name='cambiar_contraseña')
]
