from django.urls import path
from .views import AutenticacionAPI

urlpatterns = [
    path('api/autenticacion/', AutenticacionAPI.as_view(), name='autenticacion-api'),
]