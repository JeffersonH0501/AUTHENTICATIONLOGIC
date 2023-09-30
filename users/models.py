from django.db import models

class User(models.Model):
    usuario = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)