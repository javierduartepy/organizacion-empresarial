from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import PersonaUsuario

# 👥 1. Vista para ver la lista de Empleados cargados
class PersonaListView(ListView):
    model = PersonaUsuario
    template_name = 'personas/persona_list.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        # Excluimos al superusuario oculto del sistema para mostrar solo personal formal
        return PersonaUsuario.objects.filter(is_superuser=False).order_by('last_name')

# 📝 2. Vista para el Formulario de Alta con los campos solicitados
class PersonaCreateView(CreateView):
    model = PersonaUsuario
    template_name = 'personas/persona_form.html'
    # Campos obligatorios del formulario de alta
    fields = ['username', 'password', 'first_name', 'last_name', 'dni', 'area']
    success_url = reverse_lazy('personas:lista')

    def form_valid(self, form):
        # Encriptamos la contraseña antes de guardar en la base de datos
        usuario = form.save(commit=False)
        usuario.set_password(form.cleaned_data['password'])
        usuario.save()
        
        messages.success(self.request, f"¡Empleado {usuario.get_full_name()} incorporado con éxito al sistema!")
        return super().form_valid(form)

