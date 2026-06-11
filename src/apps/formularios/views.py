from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import FormularioTemplate

# 📋 1. Vista para Listar las plantillas de Formularios existentes
class FormularioListView(ListView):
    model = FormularioTemplate
    template_name = 'formularios/formulario_list.html'
    context_object_name = 'formularios'

# 📝 2. Vista para Crear una nueva Plantilla de Formulario con su mapeo oblicuo
class FormularioCreateView(CreateView):
    model = FormularioTemplate
    template_name = 'formularios/formulario_form.html'
    fields = ['nombre_formulario', 'tipo_documento', 'area_propietaria', 'areas_destinatarias']
    success_url = reverse_lazy('formularios:lista')

    def form_valid(self, form):
        messages.success(self.request, "¡Plantilla de Formulario estandarizada e integrada al sistema!")
        return super().form_valid(form)
from django.shortcuts import render

# Create your views here.
