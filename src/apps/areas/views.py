from django.views.generic import ListView
from .models import AreaEmpresa
from apps.personas.models import PersonaUsuario
from apps.formularios.models import FormularioTemplate

class ListaAreasDetalleView(ListView):
    model = AreaEmpresa
    template_name = 'areas/lista_areas_detalle.html'
    context_object_name = 'areas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Detectamos si el usuario seleccionó un área de la lista en la pantalla
        area_id = self.request.GET.get('area_id')
        
        if area_id:
            try:
                area_seleccionada = AreaEmpresa.objects.get(id=area_id)
                context['area_seleccionada'] = area_seleccionada
                
                # 1. Traemos el talento humano adscripto a este sector (Unidad 3)
                context['personal'] = PersonaUsuario.objects.filter(area=area_seleccionada)
                
                # 2. Formularios propios creados por el área (Autoridad de Línea)
                context['formularios_propios'] = FormularioTemplate.objects.filter(area_propietaria=area_seleccionada)
                
                # 3. Formularios compartidos con esta área (Comunicación Oblicua / Cruzada)
                context['formularios_asociados'] = FormularioTemplate.objects.filter(areas_destinatarias=area_seleccionada)
            except AreaEmpresa.DoesNotExist:
                pass
                
        return context
