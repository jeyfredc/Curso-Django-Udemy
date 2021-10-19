from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class PruebaView(TemplateView):
    template_name= 'prueba.html'