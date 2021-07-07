from django.urls import path
from .views import *



urlpatterns=[
    path('', ventanaprincipal, name="ventanaprincipal"),
    path('mostrar',mostrar, name="mostrar"),
    path('anadir', anadir, name="anadir"),
    path('modificar/<id>',modificar, name="modificar"),
    path('anadir', anadir, name="anadir"),
    path('eliminar <id> ',eliminar, name="eliminar"),
    
]


