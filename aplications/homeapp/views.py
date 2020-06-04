from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView
from .models import Prueba

# Create your views here.

class PruebaView(TemplateView):

    template_name='home/prueba.html'



class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0','10','20','30']

class ListarPrueba(ListView):
    template_name='home/lista_prueba.html'
    model=Prueba
    context_object_name='lista'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    fields=['titulo','subtitulo','cantidad']

    




