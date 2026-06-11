from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import DocumentoPDF

@admin.register(DocumentoPDF)
class DocumentoPDFAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'formulario', 'fecha_creacion', 'is_archivado')
    list_filter = ('is_archivado', 'formulario__tipo_documento')
    search_fields = ('nombre', 'formulario__nombre_formulario')
    
    # Desactivamos la acción nativa de Django de "Eliminar filas seleccionadas" por seguridad
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    # Bloqueamos el botón de borrado individual adentro del formulario web
    def has_delete_permission(self, request, obj=None):
        return False

    # Creamos las dos acciones personalizadas para la lista masiva de Django
    actions = ['marcar_como_archivado', 'recuperar_de_archivados']

    @admin.action(description="📦 Archivar documentos seleccionados")
    def marcar_como_archivado(self, request, queryset):
        filas_actualizadas = queryset.update(is_archivado=True)
        self.message_user(request, f"Se archivaron con éxito {filas_actualizadas} documentos.")

    @admin.action(description="♻️ Recuperar documentos seleccionados")
    def recuperar_de_archivados(self, request, queryset):
        filas_recuperadas = queryset.update(is_archivado=False)
        self.message_user(request, f"Se recuperaron con éxito {filas_recuperadas} documentos.")

