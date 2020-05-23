from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Projet(models.Model):
    nom = models.CharField(max_length=100)

    class Meta:
        verbose_name = "projet"

    def __str__(self):
        return self.nom

class Statut(models.Model):
    nom = models.CharField(max_length=50)
    couleur = models.CharField(max_length=50)

    class Meta:
        verbose_name = "statut"

    def __str__(self):
        return self.nom

class Tache(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    start = models.DateField(default=timezone.now)
    end = models.DateField(default=timezone.now)
    priority = models.IntegerField(default=1)
    assigned = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey('Statut', on_delete=models.CASCADE)
    projet = models.ForeignKey('Projet', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "tache"

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    texte = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    tache = models.ForeignKey('Tache', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "commentaire"

    def __str__(self):
        return self.texte[:40]+"..."