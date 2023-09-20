from django.contrib import admin
from .models import Empleado, Habilidades


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 
                    'last_name', 
                    'departamento',
                    'job',
                    'full_name',
                    )
    search_fields = ('first_name', )
    list_filter = ('departamento', 'job', 'habilidades')
    
    # Search many to many
    filter_horizontal = ('habilidades',)
    
    def full_name(self, obj):
        
        return obj.first_name + ' ' + obj.last_name
        
    
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)