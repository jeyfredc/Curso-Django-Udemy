from django.contrib import admin
from django.urls import path

def ListarPersonas(self):
    print('=========Desde la app listar Personas=======')

urlpatterns = [
    path('persona/', ListarPersonas),
]

