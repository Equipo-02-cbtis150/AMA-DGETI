import django_filters
from .models import Ciudad, ProyectoSustentable

class CiudadFilter(django_filters.FilterSet):
    pais = django_filters.CharFilter(field_name='pais', lookup_expr='icontains', label='País')
    ciudad = django_filters.CharFilter(field_name='ciudad', lookup_expr='icontains', label='Ciudad')

    class Meta:
        model = Ciudad
        fields = ['pais', 'ciudad']

class ProyectoSustentableFilter(django_filters.FilterSet):
    nombre_proyecto = django_filters.CharFilter(field_name='nombre_proyecto', lookup_expr='icontains', label='Proyecto')
    ciudad = django_filters.CharFilter(field_name='ciudad', lookup_expr='icontains', label='Ciudad/País')

    class Meta:
        model = ProyectoSustentable
        fields = ['nombre_proyecto', 'ciudad']