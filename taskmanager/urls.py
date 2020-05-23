from django.urls import path
from .views import *

urlpatterns = [
    path('connect/', connect, name = "Connexion"),
    path('disconnect/', disconnect, name = "Deconnexion"),
    path('projects/', projets, name = "Projets"),
    path('project/<int:id>', projet, name = "Projet"),
    path('task/<int:id>', tache, name = "Tache"),
    path('delete-project/<int:id>/', delete_projet, name = "Suppression Projet"),
    path('delete-project-def/<int:id>/', delete_def_projet, name = "Suppression Definitive Projet"),
    path('modify-project/<int:id>/', modify_projet, name = "Modification Projet"),
    path('add-project/', add_projet, name = "Ajout Projet"),
    path('delete-tache/<int:id>/', delete_tache, name = "Suppression Tache"),
    path('delete-tache-def/<int:id>/', delete_def_tache, name = "Suppression Definitive Tache"),
    path('modify-tache/<int:id>/', modify_tache, name = "Modification Tache"),
    path('add-tache/<int:id>/', add_tache, name = "Ajout Tache"),
    path('delete-comm/<int:id>/', delete_comm, name = "Suppression Commentaire"),
    path('delete-comm-def/<int:id>/', delete_def_comm, name = "Suppression Definitive Commentaire"),
    path('modify-comm/<int:id>/', modify_comm, name = "Modification Commentaire"),
    path('add-comm/<int:id>/', add_comm, name = "Ajout Commentaire"),
    path('denied/', denied, name = "Refusé"),
]