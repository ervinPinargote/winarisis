from django.contrib import admin

# Register your models here.
from .models import ConfiguracionIndex, noticias_index


@admin.register(ConfiguracionIndex)
class cConfiguracionIndex(admin.ModelAdmin):
    list_display = ("institucion", "mision", "vision", 'correo', 'ruc')
    search_fields = ('institucion', 'ruc',)

@admin.register(noticias_index)
class noticias_index(admin.ModelAdmin):
    list_display = ("titulo", "descripcion", "imagen")
    search_fields = ('titulo', 'descripcion',)
