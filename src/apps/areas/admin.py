from django.contrib import admin
from .models import AreaEmpresa

@admin.register(AreaEmpresa)
class AreaEmpresaAdmin(admin.ModelAdmin):
    # Campos que se van a ver en la lista general de áreas
    list_display = ('id', 'nombre', 'nodo_jerarquia', 'fecha_creacion')
    
    # Buscador por nombre y por el nombre del nodo del árbol
    search_fields = ('nombre', 'nodo_jerarquia__nombre')
    
    # Ordenar por ID por defecto
    ordering = ('id',)
