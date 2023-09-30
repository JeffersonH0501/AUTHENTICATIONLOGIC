from django.http import HttpResponse
from ..models import User

def verificar_usuario(usuario, clave):
    try:
        usuario_db = User.objects.get(usuario=usuario, clave=clave)
        response_data = "VALIDO"
    except User.DoesNotExist:
        response_data = "INVALIDO"

    return HttpResponse(response_data)