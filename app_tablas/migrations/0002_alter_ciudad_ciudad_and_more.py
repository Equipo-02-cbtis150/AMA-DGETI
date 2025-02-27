# Generated by Django 5.1.2 on 2024-10-21 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tablas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='ciudad',
            field=models.CharField(max_length=100, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='indice_sostenibilidad',
            field=models.CharField(max_length=100, verbose_name='Índice de sostenibilidad'),
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='pais',
            field=models.CharField(max_length=100, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='proyectos_destacados',
            field=models.TextField(verbose_name='Proyectos destacados'),
        ),
        migrations.AlterField(
            model_name='proyectosustentable',
            name='ano_inicio',
            field=models.CharField(max_length=100, verbose_name='Año de inicio'),
        ),
        migrations.AlterField(
            model_name='proyectosustentable',
            name='ciudad',
            field=models.CharField(max_length=100, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='proyectosustentable',
            name='descripcion',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='proyectosustentable',
            name='impacto_ambiental',
            field=models.TextField(verbose_name='Impacto ambiental'),
        ),
        migrations.AlterField(
            model_name='proyectosustentable',
            name='nombre_proyecto',
            field=models.CharField(max_length=100, verbose_name='Nombre del proyecto'),
        ),
    ]
