from django.urls import path
from .views import *

urlpatterns = [
    path('connect/', connect, name = "Connexion"),
    path('disconnect/', disconnect, name = "Deconnexion"),
    path('projects/', projets, name = "Projets"),
    path('projet/<int:id>', projet, name = "Projet"),
    path('tache/<int:id>', tache, name = "Tache"),
    path('delete-project/<int:id>/', delete_projet, name = "Suppression Projet"),
    path('delete-project-def/<int:id>/', delete_def_projet, name = "Suppression Definitive Projet"),
    path('modify-project/<int:id>/', modify_projet, name = "Modification Projet"),
    path('add-project/', add_projet, name = "Ajout Projet"),
    path('denied/', denied, name = "Refusé"),
]