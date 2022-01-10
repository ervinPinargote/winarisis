from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class producto(models.Model):
    nombre_producto = models.CharField(max_length=100, null=False, verbose_name="Nombre Producto")
    desc_beneficio = models.TextField(null=False)
    fecha_registro = models.DateField(default=None)
    id_organizacion = models.ForeignKey('organizacionn.organizaciones', on_delete=models.CASCADE,
                                        verbose_name="id_organizacion")

    def __str__(self):
        return self.nombre_producto


class categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100, null=False, verbose_name="Nombre Categoria")
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_categoria


class unidad_medida(models.Model):
    unidad_medida = models.CharField(max_length=10, null=False, verbose_name="Nombre Medida")
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.unidad_medida


class presentacion(models.Model):
    nombre_presentacion = models.CharField(max_length=100, null=False, verbose_name="Nombre Presentacion")
    logo = models.ImageField(upload_to="organizaciones/productos")
    detalles = models.TextField(null=True)
    estado = models.BooleanField(default=False)
    cont_neto = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    precio_mayor = models.DecimalField(max_digits=5, decimal_places=2)
    id_unidad_medida = models.ForeignKey('unidad_medida', on_delete=models.CASCADE, verbose_name="id_unidad Medida")
    id_categoria = models.ForeignKey('categoria', on_delete=models.CASCADE, verbose_name="id_categoria")
    id_producto = models.ForeignKey('producto', on_delete=models.CASCADE, verbose_name="id_producto")

    def __str__(self):
        return self.nombre_presentacion


class calificacion(models.Model):
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    comentario = models.TextField()
    fecha_registro = models.DateField(default=None)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_presentacion = models.ForeignKey('presentacion', on_delete=models.CASCADE, verbose_name="id_presentacion")

    def __str__(self):
        return self.comentario