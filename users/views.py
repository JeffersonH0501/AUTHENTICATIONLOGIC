from users.logic.logic_users import get_users
from django.http import JsonResponse

def login_view(request):

    response_data = {'message': 'Inicio de sesión NO exitoso'}
    usuarios = get_users()

    for usuario_db in usuarios:
        if usuario_db[0] == usuario:
            if usuario_db[1] == clave:
                response_data['message'] = 'Inicio de sesión exitoso'
    
    return JsonResponse(response_data)

def users_create(request):
    #TODO
    pass