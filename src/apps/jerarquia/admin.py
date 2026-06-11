from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import NodoJerarquia

@admin.register(NodoJerarquia)
class NodoJerarquiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'padre', 'is_root')
    list_filter = ('is_root',)
    search_fields = ('nombre',)

    def delete_model(self, request, obj):
        # Captura la validación del modelo para mostrarla lindo en la interfaz web de Django
        try:
            obj.delete()
        except ValidationError as e:
            self.message_user(request, str(e), level=messages.ERROR)

    def delete_queryset(self, request, queryset):
        # Control concurrente grupal: evita borrado masivo que incluya al CEO
        if queryset.filter(is_root=True).exists():
            self.message_user(
                request, 
                "Operación cancelada: No se permite la eliminación de la Alta Gerencia de forma masiva.", 
                level=messages.ERROR
            )
            return
        queryset.delete()
