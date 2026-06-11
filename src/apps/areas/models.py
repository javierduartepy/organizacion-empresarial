from django.db import models
from apps.jerarquia.models import NodoJerarquia

class AreaEmpresa(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    
    # Conexión obligatoria Uno a Uno con el Árbol (Unidad 3: Estructura)
    # Garantiza que cada sector físico ocupe un único lugar en el organigrama
    nodo_jerarquia = models.OneToOneField(
        NodoJerarquia, 
        on_delete=models.CASCADE, 
        related_name='area_real',
        verbose_name="Nodo de Jerarquía"
    )
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Área de la Empresa"
        verbose_name_plural = "Áreas de la Empresa"

    def __str__(self):
        return f"{self.nombre}"
from django.db import models

# Create your models here.
