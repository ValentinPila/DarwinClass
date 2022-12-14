# Generated by Django 4.1.2 on 2022-10-17 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lenguaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Historia', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.TextField(max_length=300)),
                ('Experiencia', models.IntegerField()),
                ('Horas', models.IntegerField()),
                ('Contacto', models.CharField(max_length=50)),
                ('FechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('Creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Lenguaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.lenguaje')),
            ],
        ),
    ]
