import django_tables2 as tables
from .models import Ciudad, ProyectoSustentable

class CiudadTable(tables.Table):
    class Meta:
        model = Ciudad
        template_name = "django_tables2/bootstrap.html"
        fields = ("pais", "ciudad", "indice_sostenibilidad", "proyectos_destacados")

class ProyectoSustentableTable(tables.Table):
    class Meta:
        model = ProyectoSustentable
        template_name = "django_tables2/bootstrap.html"
        fields = ("nombre_proyecto", "ciudad", "descripcion", "ano_inicio", "impacto_ambiental")