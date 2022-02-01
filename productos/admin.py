from django.contrib import admin

# Register your models here.
from .models import producto, categoria, unidad_medida, presentacion, calificacion


@admin.register(producto)
class cproducto(admin.ModelAdmin):
    list_display = ("nombre_producto", "desc_beneficio", "fecha_registro", 'id_organizacion')
    search_fields = ('nombre_producto', 'id_organizacion','fecha_registro',)

@admin.register(categoria)
class ccategoria(admin.ModelAdmin):
    list_display = ("nombre_categoria", "estado")
    search_fields = ('nombre_categoria', 'estado',)

@admin.register(unidad_medida)
class cunidad_medida(admin.ModelAdmin):
    list_display = ("unidad_medida", "estado")
    search_fields = ('unidad_medida', 'estado',)

@admin.register(presentacion)
class cpresentacion(admin.ModelAdmin):
    list_display = ("nombre_presentacion", "cont_neto", "id_unidad_medida", "precio", "precio_mayor", "id_categoria","id_producto")
    search_fields = ('nombre_presentacion', 'precio', 'id_categoria', 'id_producto')

@admin.register(calificacion)
class ccalificacion(admin.ModelAdmin):
    list_display = ("id_usuario", "fecha_registro", "id_presentacion", "comentario", "porcentaje")
    search_fields = ('id_usuario', 'id_presentacion', 'fecha_registro',)
