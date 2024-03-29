from django.db import models

# Create your models here.


class OrdenVenta(models.Model):
    codigosap = models.CharField(max_length=50)
    proyecto = models.CharField(max_length=255)
    direccion_proyecto = models.TextField()
    observacion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"{self.codigosap} - {self.proyecto}"


class ItemOrdenVenta(models.Model):
    ordenventa = models.ForeignKey(
        OrdenVenta, related_name="items", on_delete=models.CASCADE
    )
    nro_articulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio_bruto = models.DecimalField(max_digits=10, decimal_places=2)
    total_bruto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nro_articulo} - {self.ordenventa}"
