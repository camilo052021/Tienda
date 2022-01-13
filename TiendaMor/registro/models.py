from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Datos(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, verbose_name="Nombre", null=True)
    ciudad = models.CharField(max_length=50,verbose_name='Ciudad')
    direccion = models.CharField(max_length=150, verbose_name="Dirección", null= True)
    celular = models.CharField(max_length=50, verbose_name="Celular", null= True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'nombre'
        verbose_name_plural = 'nombres'

    def __str__(self):
        return self.nombre