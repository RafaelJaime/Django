from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    dni = models.CharField(max_length=50, blank=True, null=True, unique=True)
    direction = models.CharField(max_length=50, blank=True, null=True, verbose_name="Direction")
    telephone = models.CharField(max_length=50, blank=True, null=True, verbose_name="Telephone")
    bornDate = models.DateField(verbose_name="Born date: ", blank=True, null=True)
    is_client = models.BooleanField(default=True)
    is_mechanic = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)