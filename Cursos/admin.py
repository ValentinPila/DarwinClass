from django.contrib import admin
from .models import Curso, Lenguaje, Comentarios

# Register your models here.

class ComentarioInLine(admin.StackedInline):
    model = Comentarios

class CursoAdmin(admin.ModelAdmin):
    inlines = [ComentarioInLine]

admin.site.register(Comentarios)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Lenguaje)