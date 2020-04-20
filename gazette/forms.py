from django import forms
from .models import Article, Commentaire

#Crée des form pour les modèles et leurs champs concernés


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('titre','auteur','mail','contenu','formatPDF','image','remarques')

class CommentaireForm(forms.ModelForm):

    class Meta:
        model = Commentaire
        fields = ('auteur','com')
