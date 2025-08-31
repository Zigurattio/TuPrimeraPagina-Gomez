from django.contrib import path
from pagina.views import inicio

urlpatterns=[
    path('vista/', inicio, name='pagina' )
]