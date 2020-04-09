import datetime

from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Article, Numero
from .forms import ArticleForm

from django.utils import timezone


#def index(request):
#    return HttpResponse("Voici la page d'acceuil de la gazette !")

def index(request):
    dernier_article = Article.objects.order_by('-pub_date')[:5]
    dernier_article = Article.objects.filter(etat="publié")
    context = {
        'dernier_article':dernier_article,
    }
    return render(request,'gazette/index.html', context)

def numero(request):
    le_numero = Numero.objects.all()
    context= {
        'le_numero':le_numero,
    }
    return render(request,'gazette/numero.html',context)

def apropos(request):
    return render(request,'gazette/apropos.html')

def culture_view(request):
    article_culture = Article.objects.filter(categorie="culture", etat="publié")
    context={
        'article_culture':article_culture,
    }
    return render(request,'gazette/culture.html', context)

def autres_view(request):
    article_culture = Article.objects.filter(categorie="autre")
    context={
        'article_culture':article_culture,
    }
    return render(request,'gazette/culture.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'gazette/detail.html', {'article':article})


def login_request(request):
    if request.method == 'POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            if user is not None :
                login(request,user)
                messages.info(request,f"vous êtes connecté ! youpi !")
                return redirect("index")
            else :
                messages.error(request,f"Mauvais mdp ou nom")
             
        else:
            messages.error(request,f"problemes lors de la connexion")
    form = AuthenticationForm()
    return render(request=request,template_name='gazette/connexion.html',context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")

def article_nouveau(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = ArticleForm()
    return render(request,'gazette/nouveau.html',{'form':form})

def img_display(request):
    myPath = "MEDIA_ROOT+'/'+str(image)"
    return render(request,'gazette/detail.html',{"myPath":myPath})
