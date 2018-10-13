from django.urls import path
from doe_fraldas import views

urlpatterns = [
    path('', views.index, name='euamovida-doe-fraldas'),
]
