from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50,blank=True)
    short_name = models.CharField('Nombre corto', max_length=50)
    anulate=models.BooleanField('Anulado',default=False)

    class Meta:
        verbose_name='Mi Departamento'
        verbose_name_plural='Areas de la empresa'
        ordering=['name']
        unique_together=('name','short_name')

    def __str__(self):
        return  self.name + '-'+ self.short_name