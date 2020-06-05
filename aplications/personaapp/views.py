from django.shortcuts import render
from django.views.generic import ListView
from .models import Empleado

# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    
#lista empleados de un area
class ListByArea(ListView):
    template_name = "persona/list_area.html"
    def get_queryset(self):
        area = self.kwargs['shortname']
        lista= Empleado.objects.filter(
            departamento__short_name=area
            )
        return lista
    
