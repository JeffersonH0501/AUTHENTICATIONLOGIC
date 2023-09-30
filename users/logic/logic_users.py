from ...loginauthentication.models import User

def get_users():
    queryset = User.objects.all()
    return (queryset)

def create_user():
    #TODO
    pass

def create_user_object():
    #TODO
    pass