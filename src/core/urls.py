from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Pantalla de Inicio / Dashboard General de ECOM
    path('', TemplateView.as_view(template_name='base/inicio.html'), name='inicio'),
    
    # Inclusión de los enrutadores de cada subsistema
    path('jerarquia/', include('apps.jerarquia.urls')),
    path('areas/', include('apps.areas.urls')),
    path('personas/', include('apps.personas.urls')),
    path('formularios/', include('apps.formularios.urls')),
    path('documentos/', include('apps.documentos.urls')),
]

