from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from apps.areas.models import AreaEmpresa

class PersonaUsuario(AbstractUser):
    # Campos obligatorios solicitados en tus issues
    dni = models.CharField(max_length=20, unique=True, verbose_name="DNI")
    
    # Selector de área real (Unidad 3: Adscripción formal a la estructura)
    area = models.ForeignKey(
        AreaEmpresa, 
        on_delete=models.PROTECT, 
        related_name='empleados',
        null=True, # Permitimos null solo para el CEO raíz de alta gerencia que maneja todo
        blank=True,
        verbose_name="Área de la Empresa",
        help_text="Área física a la que pertenece esta persona."
    )

    def save(self, *args, **kwargs):
        # Primero guardamos el usuario en la base de datos
        super().save(*args, **kwargs)
        
        # Lógica automatizada con Grupos de Django (Unidad 3: Autoridad Formal)
        # Si la persona tiene un área asignada, el sistema la ingresa
        # automáticamente al Grupo de Personas que lleva el nombre de su área.
        if self.area:
            grupo, created = Group.objects.get_or_create(name=self.area.nombre)
            self.groups.clear() # Limpiamos grupos viejos por seguridad si cambió de sector
            self.groups.add(grupo) # Hereda todos los permisos del sector

    class Meta:
        verbose_name = "Persona / Usuario"
        verbose_name_plural = "Personas / Usuarios"

    def __str__(self):
        return f"{self.last_name}, {self.first_name} (DNI: {self.dni})"

