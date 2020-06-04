from django.contrib import admin
from .models import Empleado,Habilidades
# Register your models here.


admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )

    def full_name(self,obj):
        #operaciones
        
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name',)
    list_filter = ('job','habilidades',)
#filtro para relaciones manytomany
    filter_horizontal = ('habilidades',)
admin.site.register(Empleado,EmpleadoAdmin)
