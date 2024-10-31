from django.urls import path 
from .views import CiudadListView, ProyectoSustentableListView

urlpatterns = [
    path('ciudades/', CiudadListView.as_view(), name='ciudad_list'),
    path('proyectos/', ProyectoSustentableListView.as_view(), name='proyecto_list'),
]
