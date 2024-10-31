from django.db import models

# Create your models here.

class Ciudad(models.Model):
    pais = models.CharField(max_length=100, verbose_name="País")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    indice_sostenibilidad = models.CharField(max_length=100, verbose_name="Índice de sostenibilidad")
    proyectos_destacados = models.TextField(verbose_name="Proyectos destacados")

    def _str_(self):
        return self.pais

class ProyectoSustentable(models.Model):
    nombre_proyecto = models.CharField(max_length=100, verbose_name="Nombre del proyecto")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    descripcion = models.TextField(verbose_name="Descripción")
    ano_inicio = models.CharField(max_length=100, verbose_name="Año de inicio")
    impacto_ambiental = models.TextField(verbose_name="Impacto ambiental")

    def _str_(self):
        return self.nombre_proyecto