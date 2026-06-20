from django.urls import path
from . import views

app_name = 'jerarquia'
urlpatterns = [
    # Esta única URL maneja el GET (ver árbol) y el POST (crear nodo hijo)
    path('arbol/', views.EstructuraArbolView.as_view(), name='arbol'),
]

