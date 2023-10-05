from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('users.urls')),
    path('health-check/', views.healthCheck)
]
