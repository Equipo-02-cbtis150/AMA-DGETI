from django.urls import path
from . import views

urlpatterns = [
    path('', views.AmaDGETI, name='AmaDGETI'),
    path('acerca de/', views.about, name='about'),
    path('DiaMundialdelasComunidadesyCiudadesSostenibles/', views.sostenibles, name='sostenibles'),
    path('pagina en proceso/', views.error, name='error'),
]
