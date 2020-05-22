from django.urls import path
from .views import *

urlpatterns = [
    path('connect/', connect, name = "Connexion"),
    path('disconnect/', disconnect, name = "Deconnexion"),
    path('projects/', projets, name = "Projets"),
    path('projet/<int:id>', projet, name = "Projet"),
    path('denied/', denied, name = "Refusé"),
]