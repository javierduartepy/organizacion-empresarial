from django.db import models
from django.core.exceptions import ValidationError

class NodoJerarquia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    # Un nodo apunta a otro nodo padre superior (Relación recursiva)
    # Si 'padre' es null, significa que es la punta de la pirámide (CEO)
    padre = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='hijos'
    )
    
    # Campo interno para identificar al nodo supremo
    is_root = models.BooleanField(default=False, editable=False)

    def save(self, *args, **kwargs):
        # Regla de negocio (Unidad 3): Solo puede existir un único CEO raíz
        if not self.padre:
            if NodoJerarquia.objects.filter(padre__isnull=True).exclude(pk=self.pk).exists():
                raise ValidationError("Error: Ya existe una Alta Gerencia (CEO) definida como raíz del árbol.")
            self.is_root = True
        else:
            self.is_root = False
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Regla de negocio (Unidad 3): El CEO es indestructible, sostiene el sistema
        if self.is_root:
            raise ValidationError("Acceso Denegado: No se permite la eliminación de la Alta Gerencia (CEO).")
        super().delete(*args, **kwargs)

    def __str__(self):
        if self.is_root:
            return f"👑 {self.nombre} (Alta Gerencia / Raíz)"
        return f"📁 {self.nombre} (Hijo de: {self.padre.nombre})"
