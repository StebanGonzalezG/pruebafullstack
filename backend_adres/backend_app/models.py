from django.db import models

class Adquisicion(models.Model):
    presupuesto = models.CharField(max_length=255)
    unidad = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    valor_unitario = models.FloatField()
    valor_total = models.FloatField()
    fecha_adquisicion = models.DateField()
    proveedor = models.CharField(max_length=255)
    documentacion = models.CharField(max_length=255)

    def __str__(self):
        return self.presupuesto
