from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class organizaciones(models.Model):
    identificación = models.CharField(max_length=15, null=False, verbose_name="Identificación Organizacion")
    nombre_organizacion = models.CharField(max_length=70, null=False, verbose_name="Nombre Organizacion")
    descripcion = models.TextField()
    fecha_creacion = models.DateField(default=None)
    fecha_registro = models.DateField(default=None)
    correo = models.EmailField(default="null@null.com", null=True,verbose_name="Correo")
    telefono = models.CharField(max_length=10, null=True, verbose_name="Telefono")
    direccion1 = models.TextField(null=False, verbose_name="Direccion 1")
    direccion2 = models.TextField(null=True, verbose_name="Direccion 2")
    logo = models.ImageField(upload_to="organizaciones/logos")

    def __str__(self):
        return self.nombre_organizacion

class tipo_autoridad(models.Model):
    cod = models.CharField(max_length=4, null=False, verbose_name="cod")
    descripcion = models.CharField(max_length=30, null=False, verbose_name="cod")

    def __str__(self):
        return self.descripcion

class autoridades_organizacion(models.Model):
    ci = models.CharField(max_length=15, null=False, verbose_name="Identificación")
    nombre_apellido = models.CharField(max_length=70, null=False, verbose_name="Nombres y Apellidos")
    telefono = models.CharField(max_length=10, null=True, verbose_name="Telefono")
    correo = models.EmailField(default="null@null.com", null=True,verbose_name="Correo")
    id_organizacion = models.ForeignKey('organizaciones', on_delete=models.CASCADE, verbose_name="Organizacion")
    id_tipo_autoridad = models.ForeignKey('tipo_autoridad', on_delete=models.CASCADE, verbose_name="Tipo autoridad")

class redes_sociales(models.Model):
    link = models.URLField()
    mask = models.CharField(max_length=15, null=False, verbose_name="Maskara web")
    id_organizacion = models.ForeignKey('organizaciones', on_delete=models.CASCADE, verbose_name="Organizacion")

class usuarios_organizacion(models.Model):
    id_organizacion = models.ForeignKey('organizaciones', on_delete=models.CASCADE, verbose_name="Organizacion")
    id_usuarios = models.ForeignKey(User, on_delete=models.CASCADE)