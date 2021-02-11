from django.db import models
# Create your models here.

class reparation(models.Model):
    FechaSolicitud = models.DateTimeField(auto_now_add=True)
    FechaArreglo = models.DateTimeField(auto_now=True, blank=True, null=True)
    Motivo = models.CharField(max_length=500)
    Observaciones = models.CharField(max_length=500, blank=True, null=True)
    Arreglado = models.BooleanField(default=False)
    Coche = models.ForeignKey("cars.coche", on_delete=models.CASCADE, verbose_name="Coche")
    Dueno = models.ForeignKey("account.User", on_delete=models.CASCADE, verbose_name="Dueno")
    Mecanico = models.ForeignKey("account.User", on_delete=models.CASCADE, verbose_name="Mecanico", related_name='mecanico', blank=True, null=True)