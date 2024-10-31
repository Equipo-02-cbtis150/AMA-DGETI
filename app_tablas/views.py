from django.shortcuts import render
from .models import Ciudad, ProyectoSustentable
from .tables import CiudadTable, ProyectoSustentableTable
from .filters import CiudadFilter, ProyectoSustentableFilter
import django_tables2 as tables

class CiudadListView(tables.SingleTableView):
    model = Ciudad
    table_class = CiudadTable
    template_name = 'app_tablas/ciudades.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CiudadFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

class ProyectoSustentableListView(tables.SingleTableView):
    model = ProyectoSustentable
    table_class = ProyectoSustentableTable
    template_name = 'app_tablas/proyectos.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProyectoSustentableFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context