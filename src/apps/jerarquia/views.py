from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import NodoJerarquia

# 🌳 1. Vista para Listar y Renderizar el Árbol Estructural
class EstructuraArbolView(ListView):
    model = NodoJerarquia
    template_name = 'jerarquia/estructura_arbol.html'
    context_object_name = 'nodos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Traemos solo el nodo raíz (CEO) para arrancar la renderización recursiva en el HTML
        context['nodo_raiz'] = NodoJerarquia.objects.filter(padre__isnull=True).first()
        return context

# 📁 2. Vista para Crear un Nodo Hijo en la Jerarquía (Morfogénesis)
class NodoHijoCreateView(CreateView):
    model = NodoJerarquia
    fields = ['nombre', 'padre']
    template_name = 'jerarquia/estructura_arbol.html' # Reutiliza la misma pantalla
    success_url = reverse_lazy('jerarquia:arbol')

    def form_valid(self, form):
        try:
            messages.success(self.request, f"¡Nodo '{form.cleaned_data['nombre']}' creado con éxito en la estructura!")
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)
from django.shortcuts import render

# Create your views here.
