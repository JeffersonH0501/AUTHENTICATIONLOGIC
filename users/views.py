import rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User

def verificar_usuario(usuario, clave):
    try:
        usuario_db = User.objects.get(usuario=usuario, clave=clave)
        response_data = "valido"
    except User.DoesNotExist:
        response_data = "invalido"

    return response_data

def agregar_usuario(usuario, clave):
    nuevo_usuario = User(usuario=usuario, clave=clave)
    nuevo_usuario.save()
    print("usuario agregado con exito")

class AutenticacionAPI(APIView):

    def post(self, request):

        usuario = request.data.get('usuario')
        clave = request.data.get('clave')

        respuesta = verificar_usuario(usuario, clave)

        respuesta_post = {'respuesta': respuesta}

        return Response(respuesta_post, status=status.HTTP_200_OK)
