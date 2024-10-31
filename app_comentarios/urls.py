from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_comentarios, name='lista_comentarios'),
    path('agregar/', views.agregar_comentario, name='agregar_comentario')
]
