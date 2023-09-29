from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('usuario', 'clave')
        model = models.User