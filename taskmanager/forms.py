from django import forms
from .models import Projet, Tache, Commentaire, Statut
from django.contrib.auth.models import User
from django.utils import timezone

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

class FilterTacheForm(forms.Form):
    assigned = forms.ModelChoiceField(queryset=User.objects.all(), label="Assigné à", required=False)
    status = forms.ModelChoiceField(queryset=Statut.objects.all(), label="Statut", required=False)
    comm_select = forms.CharField(label='Commencé', widget=forms.RadioSelect(choices=[
        ('avant', "Avant"),
        ('apres', "Après"),
    ]), )
    comm_date = forms.DateField(label='le', widget=DateInput(), required=False)
    term_select = forms.CharField(label='Terminé', widget=forms.RadioSelect(choices=[
        ('avant', "Avant"),
        ('apres', "Après"),
    ]))
    term_date = forms.DateField(label='le', widget=DateInput(), required=False)
    sort_by = forms.CharField(label='Trié par', widget=forms.Select(choices=[
        ('titre', "Nom"),
        ('assigned', "Assigné à"),
        ('priority', "Priorité"),
        ('status', "Statut"),
        ('start', "Date de début"),
        ('end', "Date de fin"),
    ]))
    sort_order = forms.CharField(label='dans l\'ordre', widget=forms.RadioSelect(choices=[
        ('croiss', "Croissant"),
        ('decroiss', "Decroissant"),
    ]))