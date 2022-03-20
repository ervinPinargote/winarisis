from django.contrib import admin

# Register your models here.
from .models import producto, categoria, unidad_medida, presentacion, calificacion


@admin.register(producto)
class cproducto(admin.ModelAdmin):
    list_display = ("nombre_producto", "desc_beneficio", "fecha_registro", 'id_organizacion')
    search_fields = ('nombre_producto', 'id_organizacion__nombre_organizacion','fecha_registro',)

    list_filter = ('nombre_producto',)

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
    search_fields = ('nombre_presentacion', 'precio', 'id_unidad_medida__unidad_medida', 'id_categoria__nombre_categoria', 'id_producto__nombre_producto')

    list_filter = ('id_categoria__nombre_categoria',)

@admin.register(calificacion)
class ccalificacion(admin.ModelAdmin):
    list_display = ("id_usuario", "fecha_registro", "id_presentacion", "comentario", "porcentaje")
    search_fields = ('id_usuario__username', 'id_presentacion__nombre_presentacion', 'porcentaje', 'fecha_registro',)
