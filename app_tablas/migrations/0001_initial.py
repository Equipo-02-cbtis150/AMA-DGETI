# Generated by Django 5.1.2 on 2024-10-18 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('indice_sostenibilidad', models.CharField(max_length=100)),
                ('proyectos_destacados', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProyectoSustentable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('ano_inicio', models.CharField(max_length=100)),
                ('impacto_ambiental', models.TextField()),
            ],
        ),
    ]
