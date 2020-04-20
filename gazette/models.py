import datetime

from django.db import models
from django.utils import timezone


class Article(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=200)
    mail = models.EmailField(blank=True, null=True)
    pub_date = models.DateTimeField('date de publication')
    numero = models.CharField(max_length=200)
    categorie = models.CharField(max_length=200, default="")
    contenu = models.TextField(max_length=200000, blank=True, null=True)
    image = models.ImageField(upload_to='image_publie', blank=True, null=True)
    formatPDF = models.FileField(upload_to='articlePDF', blank=True, null=True)
    remarques = models.TextField(max_length=200000,blank=True,null=True)
    etat = models.CharField(max_length=100, default="non-publié")
    
    def __str__(self):
        return self.titre

    def was_published_recently(self):
        return self.pub_date >= timezone.now() -datetime.timedelta(days=7)

class Numero(models.Model):
    titre = models.CharField(max_length=200)
    num = models.FileField(upload_to='fichier', blank=True, null=True)
    pub_date = models.DateTimeField('date de publication')
    illustration = models.ImageField(upload_to='images/illustration', blank=True, null=True)

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    auteur = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date de publication')
    com = models.TextField(blank=True, null=True)
    etat = models.CharField(max_length=200, default='non-publié')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.auteur