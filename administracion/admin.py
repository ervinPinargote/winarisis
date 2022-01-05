from django.contrib import admin

# Register your models here.
from .models import ConfiguracionIndex, noticias_index


@admin.register(ConfiguracionIndex)
class cConfiguracionIndex(admin.ModelAdmin):
    list

@admin.register(noticias_index)
class noticias_index(admin.ModelAdmin):
    list
