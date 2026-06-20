from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from .models import NodoJerarquia

class EstructuraArbolView(ListView):
    model = NodoJerarquia
    template_name = 'jerarquia/estructura_arbol.html'
    context_object_name = 'nodos'

    def get_queryset(self):
        # Optimización: trae de antemano el padre para evitar consultas secuenciales
        return NodoJerarquia.objects.select_related('padre').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Trae el nodo raíz y sus hijos a la caché
        context['nodo_raiz'] = NodoJerarquia.objects.filter(padre__isnull=True).prefetch_related('hijos').first()
        return context

    # SOLUCIÓN AL ERROR 405: Agregamos el método POST para procesar el formulario de creación
    def post(self, request, *args, **kwargs):
        nombre = request.POST.get('nombre')
        padre_id = request.POST.get('padre')
        
        try:
            padre_nodo = NodoJerarquia.objects.get(id=padre_id)
            nuevo_nodo = NodoJerarquia(nombre=nombre, padre=padre_nodo)
            nuevo_nodo.save()
            messages.success(request, f"¡Área '{nombre}' integrada con éxito como hijo de '{padre_nodo.nombre}'!")
        except Exception as e:
            messages.error(request, f"Error al integrar el nodo: {str(e)}")
            
        return redirect('jerarquia:arbol')
