from django.db import models

# Create your models here.

class coche(models.Model):
    Matricula = models.CharField(max_length=10, unique=True, verbose_name="Matrícula")
    Marca = models.CharField(max_length=50, blank=True, null=True)
    Modelo = models.CharField(max_length=50, blank=True, null=True)
    Color = models.CharField(max_length=50, blank=True, null=True)
    FechaMatriculacion = models.DateField(verbose_name="Fecha de la matriculación")
    Imagen = models.ImageField(upload_to='coches/', blank=True, null=True)
    Dueno = models.ForeignKey("account.User", on_delete=models.CASCADE, verbose_name="Dueño")
    def __str__(self):
        return self.Matricula