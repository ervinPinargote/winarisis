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

