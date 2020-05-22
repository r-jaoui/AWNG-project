from django.contrib import admin
from django.utils.text import Truncator
from .models import *

# Register your models here.

class StatutAdmin(admin.ModelAdmin):
    list_display = ('nom', 'couleur',)
    list_filter = ('nom', )
    ordering = ('nom', )
    search_fields = ('nom', )

class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    list_filter = ('nom',)
    ordering = ('nom',)
    search_fields = ('nom',)

class TacheAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description_short', 'priority', 'projet', 'start', 'end')
    list_filter = ('priority', 'projet')
    date_hierarchy = 'start'
    ordering = ('titre', 'priority', 'projet', 'start', 'end')
    search_fields = ('titre', 'priority', 'projet')

    fieldsets = (
        ('General', {
            'fields': ('titre', 'description', 'priority',)
        }),
        ('Projet', {
            'classes':['collapse', ],
            'fields': ('projet', 'start', 'end', 'assigned', 'status', )
        }),
    )

    def description_short(self, tache):
        return Truncator(tache.description).chars(30, truncate='...')


class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('date', 'texte_short', 'tache', 'user')
    list_filter = ('tache', 'user')
    date_hierarchy = 'date'
    ordering = ('date', 'user', 'texte', 'tache', )
    search_fields = ('texte', 'tache', 'user')

    def texte_short(self, commentaire):
        return Truncator(commentaire.texte).chars(30, truncate='...')

admin.site.register(Projet, ProjetAdmin)
admin.site.register(Statut, StatutAdmin)
admin.site.register(Tache, TacheAdmin)
admin.site.register(Commentaire, CommentaireAdmin)