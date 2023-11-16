import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario

def verificar_usuario(documento, clave):

    try:
        usuario = Usuario.objects.get(documento=documento, clave=clave)
    except Usuario.DoesNotExist:
        usuario = None

    return usuario

class AutenticacionAPI(APIView):

    def post(self, request):
        
        documento = request.data.get("documento")
        clave = request.data.get("clave")

        usuario = verificar_usuario(documento, clave)

        if usuario is not None:

            token_payload = {"documento": usuario.documento, "tipo": usuario.tipo}
            token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm="HS256")

            respuesta_post = {"token": token}
        else:
            respuesta_post = {}

        return Response(respuesta_post, status=status.HTTP_200_OK)