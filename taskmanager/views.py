from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required
from .forms import *
from .models import *

# Create your views here.
def connect(request):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    form = ConnectForm(request.POST or None)
    error = False
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
        return redirect(projets)
    else:
        if form.is_valid():
            error = True
            username = form.cleaned_data['utilisateur']
            password = form.cleaned_data['mdp']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(projets)
            else:
                pass
    return render(request, 'taskmanager/connect.html', locals())

def disconnect(request):
    connected = request.user.is_authenticated
    if connected:
        logout(request)
    return redirect(connect)

def denied(request):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    projets_list = None
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
    return render(request, 'taskmanager/denied.html', locals())


def projets(request):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    projets_list = []
    projets_taches_nbre = []
    projets = []
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
        if request.user.has_perm('taskmanager.view_projet'):
            projets_list = list(Projet.objects.all())
            for projet in projets_list:
                projets_taches_nbre.append(0)
                for tache in Tache.objects.all():
                    if tache.projet == projet:
                        projets_taches_nbre[-1]+=1
                projets.append([projet, projets_taches_nbre[-1]])
        else:
            return redirect(denied)
    else:
        return redirect(connect)
    return render(request, 'taskmanager/projects.html', locals())


def projet(request, id):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    projet = None
    taches = None
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
        if request.user.has_perm('taskmanager.view_projet') and request.user.has_perm('taskmanager.view_tache'):
            projet = Projet.objects.get(id=id)
            taches = Tache.objects.filter(projet = projet)
        else:
            return redirect(denied)
    else:
        return redirect(connect)
    return render(request, 'taskmanager/projet.html', locals())

def tache(request, id):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    tache = None
    commentaires = None
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
        if request.user.has_perm('taskmanager.view_commentaire') and request.user.has_perm('taskmanager.view_tache'):
            tache = Tache.objects.get(id=id)
            commentaires = Commentaire.objects.filter(tache = tache).order_by('date')
        else:
            return redirect(denied)
    else:
        return redirect(connect)
    return render(request, 'taskmanager/tache.html', locals())