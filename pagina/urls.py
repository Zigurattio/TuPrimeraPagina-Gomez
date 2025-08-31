from django.urls import path
from pagina.views import inicio, crear_cigarro, listado_cigarros

urlpatterns=[
    path('', inicio, name='pagina'),
    path('cigarro/crear/', crear_cigarro, name='crear_cigarro'),
    path('cigarro/listado/', listado_cigarros, name='listado_de_cigarros') 
]