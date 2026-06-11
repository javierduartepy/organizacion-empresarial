from django.urls import path
from . import views

app_name = 'documentos'
urlpatterns = [
    path('lista/', views.DocumentoListView.as_view(), name='lista'),
    path('archivados/', views.DocumentoArchivadoListView.as_view(), name='archivados'),
    path('<int:pk>/archivar/', views.ArchivarDocumentoView.as_view(), name='archivar'),
    path('<int:pk>/recuperar/', views.RecuperarDocumentoView.as_view(), name='recuperar'),
]
