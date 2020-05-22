from django.urls import path
from .views import *

urlpatterns = [
    path('connect/', connect, name = "Connexion"),
    path('disconnect/', disconnect, name = "Deconnexion"),
]