from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth.models import Permission
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
            modify = request.user.has_perm('taskmanager.change_projet')
            add = request.user.has_perm('taskmanager.add_projet')
            delete = request.user.has_perm('taskmanager.delete_projet')
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
        modify_projet = request.user.has_perm('taskmanager.change_projet')
        modify_tache = request.user.has_perm('taskmanager.change_tache')
        add_tache = request.user.has_perm('taskmanager.add_tache')
        delete_tache = request.user.has_perm('taskmanager.delete_tache')
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
        if request.user.has_perm('taskmanager.view_tache'):
            modify = request.user.has_perm('taskmanager.change_tache')
            view_comments = request.user.has_perm('taskmanager.view_commentaire')
            add_comment = request.user.has_perm('taskmanager.add_commentaire')
            modify_comment = request.user.has_perm('taskmanager.change_commentaire')
            delete_comment = request.user.has_perm('taskmanager.delete_commentaire')
            tache = Tache.objects.get(id=id)
            commentaires = Commentaire.objects.filter(tache = tache).order_by('date')
        else:
            return redirect(denied)
    else:
        return redirect(connect)
    return render(request, 'taskmanager/tache.html', locals())


def taches(request):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
        if request.user.has_perm('taskmanager.view_tache'):
            modify_tache = request.user.has_perm('taskmanager.change_tache')
            delete_tache = request.user.has_perm('taskmanager.delete_tache')
            taches = Tache.objects.all()
            return render(request, "taskmanager/taches.html", locals())
        else:
            return redirect(denied)
    else:
        return redirect(connect)
    return render(request, 'taskmanager/tache.html', locals())

def utilisateur(request):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username

        groups = request.user.groups.all()
        permissions = Permission.objects.filter(user=request.user)
        taches = Tache.objects.filter(assigned=request.user)
        projects = []
        for tache in taches:
            if tache.projet not in projects:
                projects.append(tache.projet)
        return render(request, "taskmanager/user.html", locals())
    else:
        return redirect(connect)

def delete_projet(request, id):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    tache = None
    commentaires = None
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
        if request.user.has_perm('taskmanager.delete_projet'):
            project = Projet.objects.get(id=id)
            return render(request, "taskmanager/delete_project.html", locals())
        else:
            return redirect(denied)
    else:
        return redirect(connect)

def delete_def_projet(request, id):
    if request.user.is_authenticated:
        if request.user.has_perm('taskmanager.delete_projet'):
            Projet.objects.get(id=id).delete()
            return redirect(projets)
        else:
            return redirect(denied)
    else:
        return redirect(connect)

def modify_projet(request, id):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    tache = None
    commentaires = None
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
        if request.user.has_perm('taskmanager.modify_projet'):
            proj = Projet.objects.get(id=id)
            form = ModifyProjectForm(request.POST or None, instance=proj)
            if form.is_valid():
                proj.nom = form.cleaned_data['nom']
                proj.save()
                return redirect(projet, proj.id)
            return render(request, "taskmanager/modify_project.html", locals())
        else:
            return redirect(denied)
    else:
        return redirect(connect)

def add_projet(request):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    tache = None
    commentaires = None
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
        if request.user.has_perm('taskmanager.add_projet'):
            form = ModifyProjectForm(request.POST or None)
            if form.is_valid():
                proj = form.save()
                return redirect(projet, proj.id)
            return render(request, "taskmanager/add_project.html", locals())
        else:
            return redirect(denied)
    else:
        return redirect(connect)


def delete_tache(request, id):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    task = None
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
        if request.user.has_perm('taskmanager.delete_tache'):
            task = Tache.objects.get(id=id)
            return render(request, "taskmanager/delete_tache.html", locals())
        else:
            return redirect(denied)
    else:
        return redirect(connect)

def delete_def_tache(request, id):
    if request.user.is_authenticated:
        if request.user.has_perm('taskmanager.delete_tache'):
            tache = Tache.objects.get(id=id)
            proj = tache.projet
            tache.delete()
            return redirect(projet, proj.id)
        else:
            return redirect(denied)
    else:
        return redirect(connect)

def modify_tache(request, id):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
        if request.user.has_perm('taskmanager.change_tache'):
            task = Tache.objects.get(id=id)
            form = ModifyTacheForm(request.POST or None, instance=task)
            if form.is_valid():
                task = form.save()
                return redirect(tache, id)
            return render(request, "taskmanager/modify_tache.html", locals())
        else:
            return redirect(denied)
    else:
        return redirect(connect)

def add_tache(request, id):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
        if request.user.has_perm('taskmanager.add_tache'):
            proj = Projet.objects.get(id=id)
            form = NewTacheForm(request.POST or None)
            if form.is_valid():
                task = Tache()

                task.titre = form.cleaned_data['titre']
                task.description = form.cleaned_data['description']
                task.start = form.cleaned_data['start']
                task.end = form.cleaned_data['end']
                task.priority = form.cleaned_data['priority']
                task.assigned = form.cleaned_data['assigned']
                task.status = form.cleaned_data['status']
                task.projet = proj

                task.save()
                return redirect(tache, task.id)
            return render(request, "taskmanager/add_tache.html", locals())
        else:
            return redirect(denied)
    else:
        return redirect(connect)

def delete_comm(request, id):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
        if request.user.has_perm('taskmanager.delete_commentaire'):
            comm = Commentaire.objects.get(id=id)
            return render(request, "taskmanager/delete_commentaire.html", locals())
        else:
            return redirect(denied)
    else:
        return redirect(connect)

def delete_def_comm(request, id):
    if request.user.is_authenticated:
        if request.user.has_perm('taskmanager.delete_commentaire'):
            comm = Commentaire.objects.get(id=id)
            task = comm.tache
            comm.delete()
            return redirect(tache, task.id)
        else:
            return redirect(denied)
    else:
        return redirect(connect)

def modify_comm(request, id):
    connected = request.user.is_authenticated
    name = ""
    username = ""
    if connected:
        name = request.user.first_name + " " + request.user.last_name
        username = request.user.username
        if request.user.has_perm('taskmanager.change_commentaire'):
            comm = Commentaire.objects.get(id=id)
            form = ModifyCommentaireForm(request.POST or None, initial={'texte': comm.texte, 'date': comm.date, 'tache': comm.tache, 'user': comm.user})
            if form.is_valid():
                comm.texte=form.cleaned_data['texte']
                comm.date=form.cleaned_data['date']
                comm.tache=form.cleaned_data['tache']
                comm.user=form.cleaned_data['user']

                comm.save()
                return redirect(tache, comm.tache.id)
            return render(request, "taskmanager/modify_commentaire.html", locals())
        else:
            return redirect(denied)
    else:
        return redirect(connect)


def add_comm(request, id):
    if request.user.is_authenticated:
        if request.user.has_perm('taskmanager.add_commentaire'):
            task = Tache.objects.get(id=id)
            if request.POST['text']:
                if len(request.POST['text']) > 0:
                    comm = Commentaire()
                    comm.texte = request.POST['text']
                    comm.user = request.user
                    comm.date = timezone.now()
                    comm.tache = task
                    comm.save()
            return redirect(tache, task.id)
        else:
            return redirect(denied)
    else:
        return redirect(connect)
