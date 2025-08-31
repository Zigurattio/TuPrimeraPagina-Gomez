from django.urls import path
from pagina.views import inicio

urlpatterns=[
    path('vista/', inicio, name='pagina' )
]