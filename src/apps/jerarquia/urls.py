from django.urls import path
from . import views

app_name = 'jerarquia'
urlpatterns = [
    path('arbol/', views.EstructuraArbolView.as_view(), name='arbol'),
    path('arbol/crear/', views.NodoHijoCreateView.as_view(), name='crear_nodo'),
    
]
