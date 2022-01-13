from django.db import models
from registro.models import Datos

# Create your models here.

class Venta(models.Model):
    cliente=models.ForeignKey(Datos,verbose_name='Cliente', on_delete=models.CASCADE)
    producto=models.CharField(max_length=50,verbose_name='Producto')
    cantidad=models.IntegerField(verbose_name='Cantidad')
    valor_unitario=models.FloatField(verbose_name='Precio')
    valor=models.FloatField(verbose_name='Valor Compra')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ='venta'
        verbose_name_plural ='ventas'

    def __str__(self):
        return self.producto