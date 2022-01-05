from django.contrib import admin

# Register your models here.
from .models import organizaciones, tipo_autoridad, autoridades_organizacion, redes_sociales, \
    usuarios_organizacion


@admin.register(organizaciones)
class corganizaciones(admin.ModelAdmin):
    list_display = ("identificación", "nombre_organizacion", "fecha_creacion", 'correo', 'telefono')
    search_fields = ('identificación', 'nombre_organizacion',)


@admin.register(tipo_autoridad)
class ctipo_autoridad(admin.ModelAdmin):
    list_display = ("cod", "descripcion")
    search_fields = ('cod', 'descripcion',)


@admin.register(autoridades_organizacion)
class cautoridades_organizacion(admin.ModelAdmin):
    list_display = ("ci", "nombre_apellido", "telefono", 'correo', 'id_organizacion', 'id_tipo_autoridad')
    search_fields = ('ci', 'nombre_apellido',)


@admin.register(redes_sociales)
class credes_sociales(admin.ModelAdmin):
    list_display = ("link", "mask", "id_organizacion")
    search_fields = ('mask', 'id_organizacion',)


@admin.register(usuarios_organizacion)
class cusuarios_organizacion(admin.ModelAdmin):
    list_display = ("id_organizacion", "id_usuarios")
    search_fields = ('id_organizacion', 'id_usuarios',)
