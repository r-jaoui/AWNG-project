from django.contrib import admin
from .models import *

# Register your models here.

class StatutAdmin(admin.ModelAdmin):
    list_display = ('nom', 'couleur',)
    list_filter = ('Title', 'Artist',)
    ordering = ('Title', 'Artist')
    search_fields = ('Title', 'Artist')

admin.site.register(Projet)
admin.site.register(Statut)
admin.site.register(Tache)
admin.site.register(Commentaire)