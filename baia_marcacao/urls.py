from django.urls import path
from baia_marcacao import views

urlpatterns = [
    path('', views.index, name='euamovida-baia-marcacao'),
]
