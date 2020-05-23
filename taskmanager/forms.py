from django import forms
from .models import Projet

class ConnectForm(forms.Form):
    utilisateur = forms.CharField(label="Nom d'Utilisateur")
    mdp = forms.CharField(label="Mot de Passe", widget=forms.PasswordInput())

class ModifyProjectForm(forms.ModelForm):
    class Meta:
        model=Projet
        fields="__all__"