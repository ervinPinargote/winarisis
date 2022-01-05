from django.db import models


# Create your models here.
class ConfiguracionIndex(models.Model):
    institucion = models.CharField(max_length=50, null=False, verbose_name="Nombre Institucion")
    mision = models.TextField()
    vision = models.TextField()
    correo = models.EmailField(default=None)
    ruc = models.CharField(max_length=15, null=False, verbose_name="Ruc")
    logo = models.ImageField()
    logo_url = models.CharField(max_length=50, null=False, verbose_name="Url")


class noticias_index(models.Model):
    titulo = models.CharField(max_length=50, null=False, verbose_name="Titulo noticia")
    imagen = models.ImageField(upload_to="noticias")
    link = models.CharField(max_length=50, null=True, verbose_name="link")
    descripcion = models.TextField()
