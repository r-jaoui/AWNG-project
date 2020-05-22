from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *

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
    else:
        if form.is_valid():
            error = True
            username = form.cleaned_data['utilisateur']
            password = form.cleaned_data['mdp']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(connect)
            else:
                pass
    return render(request, 'taskmanager/connect.html', locals())

def disconnect(request):
    connected = request.user.is_authenticated
    if connected:
        logout(request)
    return redirect(connect)

