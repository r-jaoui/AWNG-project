from django import forms

class ConnectForm(forms.Form):
    utilisateur = forms.CharField(label="Nom d'Utilisateur")
    mdp = forms.CharField(label="Mot de Passe", widget=forms.PasswordInput())