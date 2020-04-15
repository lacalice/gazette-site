from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    #sépare la classe en deux colonnes
    list_display = ('titre','pub_date')
    #recherche par titre
    search_fields = ('titre',)
    #filtrer par catégories
    list_filter = ('categorie',)

class AdminNum(admin.ModelAdmin):
     #sépare la classe en deux colonnes
    list_display = ('titre','pub_date')
    #recherche par titre
    search_fields = ('titre',)

admin.site.register(Article, ProjectAdmin)
admin.site.register(Numero, AdminNum)
admin.site.register(Commentaire)

