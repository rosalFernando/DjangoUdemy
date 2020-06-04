from django.db import models
from aplications.departamentoapp.models import Departamento

# Create your models here.

class Empleado(models.Model):
    #modelo para tabla empleado
    trabajos=(
        ('0','contable'),
        ('1','administrador'),
        ('2','economista'),
        ('3','otro'),
    )

    first_name=models.CharField('Nombre',max_length=60)
    last_name=models.CharField('Apellidos',max_length=60)
    job = models.CharField('Trabajo', max_length=5,choices=trabajos)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    class Meta:
        verbose_name='Empleados'
        verbose_name_plural='Area de Personal'
        ordering=['first_name']
        unique_together=('first_name','last_name')
    def __str__(self):
        return  self.first_name + '-'+ self.last_name