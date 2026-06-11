from django.urls import path
from . import views

app_name = 'personas'
urlpatterns = [
    path('alta/', views.PersonaCreateView.as_view(), name='alta'),
    path('lista/', views.PersonaListView.as_view(), name='lista'),
]
