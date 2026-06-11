from django.urls import path
from . import views

app_name = 'formularios'
urlpatterns = [
    path('crear/', views.FormularioCreateView.as_view(), name='crear'),
    path('lista/', views.FormularioListView.as_view(), name='lista'),
]
