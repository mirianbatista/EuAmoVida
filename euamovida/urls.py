"""euamovida URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from cg import views
from riotinto import views
from mamanguape import views
from baia_marcacao import views
from guarabira import views
from itapororoca import views
from jacarau import views
from doe_sangue import views
from doe_alimentos import views
from doe_fraldas import views
from doe_cereais import views
from seja_voluntario import views
from compre_camisa import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', include('home.urls')),
    path('campanha2019/', include('campanha2019.urls')),
    path('colabore/', include('colabore.urls')),
    path('ondeestamos/', include('ondeestamos.urls')),
    path('sobre/', include('sobre.urls')),
    path('contato/', include('contato.urls')),
    path('lojinha/', include('lojinha.urls')),
    path('cg/', include('cg.urls')),
    path('riotinto/', include('riotinto.urls')),
    path('mamanguape/', include('mamanguape.urls')),
    path('baia_marcacao/', include('baia_marcacao.urls')),
    path('itapororoca/', include('itapororoca.urls')),
    path('jacarau/', include('jacarau.urls')),
    path('guarabira/', include('guarabira.urls')),
    path('doe_sangue/', include('doe_sangue.urls')),
    path('doe_alimentos/', include('doe_alimentos.urls')),
    path('doe_fraldas/', include('doe_fraldas.urls')),
    path('doe_cereais/', include('doe_cereais.urls')),
    path('compre_camisa/', include('compre_camisa.urls')),
    path('seja_voluntario/', include('seja_voluntario.urls')),
    path('checkout/', include('checkout.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


