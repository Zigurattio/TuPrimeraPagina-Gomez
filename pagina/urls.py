from django.urls import path
from pagina.views import inicio, crear_cigarro, listado_cigarros , detalle_cigarro

urlpatterns=[
    path('', inicio, name='pagina'),
    path('cigarro/crear/', crear_cigarro, name='crear_cigarro'),
    path('cigarro/listado/', listado_cigarros, name='listado_de_cigarros'),
    path('cigarro/<cigarro_id>/', detalle_cigarro, name='detalle_cigarro'),
]