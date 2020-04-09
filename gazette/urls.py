from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('connexion/', views.login_request, name='connexion'),
    path('index', views.logout_request, name='logout'),
    path('culture/', views.culture_view, name='culture'),
    path('autres/', views.autres_view, name='autres'),
    path('apropos.html', views.apropos, name='apropos'),
    path('numero', views.numero, name='numero'),
    path('nouveau.html', views.article_nouveau, name='article_nouveau'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
