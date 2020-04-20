import datetime
from django.test import TestCase
from gazette.models import Article, Commentaire, Numero
from django.utils import timezone



class GazetteTest(TestCase):

#test pour vérifier si on peut ajouter un article
    def create_article(self, titre='test article',auteur='lcalice',contenu='blabla', etat='publié', categorie='culture'):
        return Article.objects.create(titre=titre,
        auteur=auteur,
        contenu=contenu,
        pub_date=timezone.now(),
        categorie=categorie,
        etat=etat)
    
    def test_article_creation(self):
        a=self.create_article()
        self.assertTrue(isinstance(a,Article))
    
    #test pour vérifier si on peut ajouter un commentaire
    def create_commentaire(self, auteur='lcalice',com='blabla',etat='publié',article=Article.objects.get(id=1)):
        return Commentaire.objects.create(auteur=auteur,
        com=com,
        etat=etat,
        article=article,
        pub_date=timezone.now())

    def test_commentaire_creation(self):
        b=self.create_commentaire()
        self.assertTrue(isinstance(b,Commentaire))

#test pour vérifier si on peut ajouter un numéro
    def  create_numero(self, titre='titre test',num='test.pdf',illustration='illu.png'):
        return Numero.objects.create(titre=titre,
        num=num,
        illustration=illustration,
        pub_date=timezone.now())

    def test_numero_creation(self):
        c=self.create_numero()
        self.assertTrue(isinstance(c,Numero))
