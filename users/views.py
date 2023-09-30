from .models import User

def verificar_usuario(usuario, clave):
    try:
        usuario_db = User.objects.get(usuario=usuario, clave=clave)
        response_data = "VALIDO"
    except User.DoesNotExist:
        response_data = "INVALIDO"

    return response_data

def agregar_usuario(usuario, clave):
    nuevo_usuario = User(usuario=usuario, clave=clave)
    nuevo_usuario.save()
    print("usuario agregado con exito")