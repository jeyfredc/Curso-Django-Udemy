from django.contrib import admin
from django.urls import path

def ListarDepartamentos(self):
    print('=========Desde la app listar departamentos=======')

urlpatterns = [
    path('departamento/', ListarDepartamentos),
]

