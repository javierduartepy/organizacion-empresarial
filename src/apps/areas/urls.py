from django.urls import path
from . import views

app_name = 'areas'
urlpatterns = [
    path('lista/', views.ListaAreasDetalleView.as_view(), name='lista'),
]
