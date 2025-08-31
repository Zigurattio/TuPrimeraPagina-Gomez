from django.urls import path
from pagina.views import inicio

urlpatterns=[
    path('', inicio, name='pagina' )
]