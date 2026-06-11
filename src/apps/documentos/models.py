from django.db import models
from django.core.exceptions import ValidationError
from apps.formularios.models import FormularioTemplate

class DocumentoPDF(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Documento")
    
    # Campo para la carga física del PDF
    archivo_pdf = models.FileField(upload_to='documentos_pdf/', verbose_name="Archivo PDF")
    
    # Se asocia obligatoriamente al Formulario (Hereda Tipo y Área de ahí)
    formulario = models.ForeignKey(
        FormularioTemplate, 
        on_delete=models.CASCADE, 
        related_name='documentos_cargados',
        verbose_name="Formulario / Plantilla"
    )
    
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    
    # LA CLAVE (Control de Activos - Unidad 3): Campo para el archivado lógico
    is_archivado = models.BooleanField(
        default=False, 
        verbose_name="¿Está Archivado?",
        help_text="Si está marcado, el documento se oculta de la lista general y pasa al archivo de recuperación."
    )

    # 🚫 REG LA DE NEGOCIO IMPRESCINDIBLE: Se prohíbe la eliminación física del registro
    def delete(self, *args, **kwargs):
        raise ValidationError(
            "Acceso Denegado: Los documentos de la empresa ECOM no se pueden eliminar del sistema, únicamente archivar."
        )

    # Métodos limpios para controlar el estado por código
    def archivar(self):
        self.is_archivado = True
        self.save()

    def recuperar(self):
        self.is_archivado = False
        self.save()

    class Meta:
        verbose_name = "Documento PDF"
        verbose_name_plural = "Documentos PDF"

    def __str__(self):
        estado = "⚠️ ARCHIVADO" if self.is_archivado else "✅ ACTIVO"
        return f"📄 {self.nombre} ({estado})"

