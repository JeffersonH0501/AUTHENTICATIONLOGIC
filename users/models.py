from django.db import models

class User(models.Model):
    usuario = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)

    def _list_(self):
        return [self.usuario, self.clave]
