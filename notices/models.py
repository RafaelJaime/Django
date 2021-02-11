from django.db import models

# Create your models here.
class noticia(models.Model):
    Titulo = models.CharField(max_length=100, verbose_name="Titulo")
    Texto = models.TextField(blank=True, null=True)
    Foto = models.ImageField(upload_to='noticias/', blank=True, null=True)
    Autor = models.ForeignKey("account.User", on_delete=models.CASCADE, blank=True, null=True)
    Fcreacion = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Fecha de cración")
    Fmodificacion = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Fecha de modificación")
    def __str__(self):
        return self.Titulo