from django.contrib import admin

# Register your models here.
from .models import ConfiguracionIndex


@admin.register(ConfiguracionIndex)
class cConfiguracionIndex(admin.ModelAdmin):
    list
