from django import forms
from .models import Projet, Tache, Commentaire

class DateInput(forms.DateInput):
    input_type = 'date'

class ConnectForm(forms.Form):
    utilisateur = forms.CharField(label="Nom d'Utilisateur")
    mdp = forms.CharField(label="Mot de Passe", widget=forms.PasswordInput())

class ModifyProjectForm(forms.ModelForm):
    class Meta:
        model=Projet
        fields="__all__"

class ModifyTacheForm(forms.ModelForm):
    class Meta:
        model=Tache
        fields="__all__"
        widgets = {
            'start': DateInput(),
            'end': DateInput()
        }

class ModifyCommentaireForm(forms.ModelForm):
    class Meta:
        model=Commentaire
        fields="__all__"

class NewTacheForm(forms.ModelForm):
    class Meta:
        model=Tache
        exclude = ('projet',)