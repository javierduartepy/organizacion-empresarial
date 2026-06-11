from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PersonaUsuario

@admin.register(PersonaUsuario)
class PersonaUsuarioAdmin(UserAdmin):
    # Agregar tus campos personalizados a los formularios del panel
    fieldsets = UserAdmin.fieldsets + (
        ('Información Corporativa', {'fields': ('dni', 'area')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Corporativa', {'fields': ('dni', 'area', 'first_name', 'last_name', 'email')}),
    )
    
    # Columnas que se van a ver en la lista general de usuarios
    list_display = ('username', 'last_name', 'first_name', 'dni', 'area', 'is_staff')
    search_fields = ('username', 'last_name', 'first_name', 'dni', 'area__nombre')
    list_filter = ('area', 'is_staff', 'is_superuser')
