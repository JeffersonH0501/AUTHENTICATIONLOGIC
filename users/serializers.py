from rest_framework import serializers
from ..loginauthentication import models

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('usuario', 'clave')
        model = models.User