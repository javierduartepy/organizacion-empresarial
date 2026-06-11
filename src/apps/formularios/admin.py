from django.contrib import admin
from .models import FormularioTemplate

@admin.register(FormularioTemplate)
class FormularioTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_formulario', 'tipo_documento', 'area_propietaria', 'fecha_creacion')
    list_filter = ('tipo_documento', 'area_propietaria')
    search_fields = ('nombre_formulario', 'area_propietaria__nombre')
    
    # Usar un selector más cómodo en el panel para la relación ManyToMany de las áreas
    filter_horizontal = ('areas_destinatarias',)
