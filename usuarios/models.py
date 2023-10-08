from django.db import models

class Usuario(models.Model):
    documento = models.CharField(max_length=15)
    clave = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)