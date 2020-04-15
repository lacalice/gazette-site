from django import forms
from .models import Article, Commentaire

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('titre','auteur','mail','contenu','formatPDF','image','remarques')

class CommentaireForm(forms.ModelForm):

    class Meta:
        model = Commentaire
        fields = ('auteur','com')
