from getpass import getuser
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

"""
Modelos:
Course:
Nombre 50 caracteres
Descripción 300 
Creador:  el usuario que esta creando el curso
Años de experiencia: numero
Lenguaje: Relacion con otro modelo (puede escogerlo)
Horas: Numero 
Link de contacto: un link de contacto puede ser de YouTube, Twitter, etc 
Fecha de creación: auto asignado (revisar que la hora lo registre bien)

Lenguaje:
Nombre 
Historia:
"""
class Lenguaje(models.Model):
    Nombre = models.CharField(max_length=50)
    Historia = models.TextField(max_length=200)

    def __str__(self):
        return self.Nombre

class Curso(models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=300)
    Creador = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Experiencia = models.IntegerField()
    Lenguaje = models.ForeignKey(Lenguaje, on_delete=models.CASCADE)
    Horas = models.IntegerField()
    Contacto = models.CharField(max_length=50)
    FechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('curso')

class Comentarios(models.Model):
    curso = models.ForeignKey(
        Curso,
        on_delete = models.CASCADE,
        related_name='comentarios',
    )
    comentario = models.CharField(max_length=200)
    creador = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('curso')