from django.db import models
from apps.areas.models import AreaEmpresa

class FormularioTemplate(models.Model):
    # Tipos de documentos estándar de la empresa
    TIPO_CHOICES = [
        ('MEMO', 'Memorándum Interno'),
        ('RESOLUCION', 'Resolución Gubernamental / Institucional'),
        ('MANUAL', 'Manual de Procedimientos / Operativo'),
        ('CIRCULAR', 'Circular General'),
    ]

    nombre_formulario = models.CharField(max_length=150, unique=True, verbose_name="Nombre del Formulario")
    tipo_documento = models.CharField(max_length=30, choices=TIPO_CHOICES, verbose_name="Tipo de Documento")
    
    # Área creadora/propietaria del formulario (Unidad 3: Autoridad Lineal)
    area_propietaria = models.ForeignKey(
        AreaEmpresa, 
        on_delete=models.CASCADE, 
        related_name='formularios_propios',
        verbose_name="Área Propietaria"
    )
    
    # LA CLAVE DE LA COMUNICACIÓN OBLICUA (Unidad 3)
    # Permite asociar este formulario a múltiples áreas destinatarias
    areas_destinatarias = models.ManyToManyField(
        AreaEmpresa, 
        blank=True, 
        related_name='formularios_recibidos',
        verbose_name="Áreas Destinatarias (Comunicación Oblicua)"
    )
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Plantilla de Formulario"
        verbose_name_plural = "Plantillas de Formularios"

    def __str__(self):
        return f"{self.nombre_formulario} [{self.get_tipo_documento_display()}]"
from django.db import models

# Create your models here.
