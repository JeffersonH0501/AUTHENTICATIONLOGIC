#import rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario

def verificar_usuario(documento, clave):
    try:
        usuario = Usuario.objects.get(usuario=documento, clave=clave)
        respuesta = "valido"
        tipo = usuario.tipo
    except Usuario.DoesNotExist:
        respuesta = "invalido"
        tipo = ""

    return respuesta, tipo

def agregar_usuario(documento, clave, tipo):
    nuevo_usuario = Usuario(documento=documento, clave=clave, tipo=tipo)
    nuevo_usuario.save()
    print("> documento: "+ documento + ", clave: " + clave + ", tipo: " + tipo + ". Agregado con exito")

class AutenticacionAPI(APIView):

    def post(self, request):

        documento = request.data.get('documento')
        clave = request.data.get('clave')

        respuesta, tipo = verificar_usuario(documento, clave)

        respuesta_post = {'respuesta': respuesta, 'tipo': tipo}

        return Response(respuesta_post, status=status.HTTP_200_OK)
    

# Codigo para agregar usuarios a la base de datos
agregar_usuario('1092524481', '123', 'profesionalSalud')
agregar_usuario('0123456789', '123', 'director')
agregar_usuario('1924203922', '123', 'paciente')
agregar_usuario('4392923920', '123', 'paciente')
agregar_usuario('2024203858', '123', 'paciente')
agregar_usuario('8693938599', '123', 'paciente')
agregar_usuario('5895863534', '123', 'paciente')
agregar_usuario('1234235439', '123', 'paciente')
agregar_usuario('2482366632', '123', 'paciente')


