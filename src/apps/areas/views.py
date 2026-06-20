from django.views.generic import ListView
from .models import AreaEmpresa
from apps.personas.models import PersonaUsuario
from apps.formularios.models import FormularioTemplate

class ListaAreasDetalleView(ListView):
    model = AreaEmpresa
    template_name = 'areas/lista_areas_detalle.html'
    context_object_name = 'areas'

    def get_queryset(self):
        # ⚡ OPTIMIZACIÓN 1: select_related hace un JOIN en SQL para traer el nodo jerárquico de un solo tiro
        return AreaEmpresa.objects.select_related('nodo_jerarquia').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        area_id = self.request.GET.get('area_id')
        
        if area_id:
            try:
                # Traemos el área y unimos su nodo jerárquico
                area_seleccionada = AreaEmpresa.objects.select_related('nodo_jerarquia').get(id=area_id)
                context['area_seleccionada'] = area_seleccionada
                
                context['personal'] = PersonaUsuario.objects.filter(area=area_seleccionada)
                
                # ⚡ OPTIMIZACIÓN 2: Al listar formularios propios, precargamos su área propietaria
                context['formularios_propios'] = FormularioTemplate.objects.filter(
                    area_propietaria=area_seleccionada
                ).select_related('area_propietaria')
                
                # ⚡ OPTIMIZACIÓN 3: prefetch_related optimiza la pasarela ManyToMany de comunicación oblicua
                context['formularios_asociados'] = FormularioTemplate.objects.filter(
                    areas_destinatarias=area_seleccionada
                ).select_related('area_propietaria').prefetch_related('areas_destinatarias')
                
            except AreaEmpresa.DoesNotExist:
                pass
                
        return context
