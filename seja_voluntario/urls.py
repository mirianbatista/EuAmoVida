from django.urls import path
from seja_voluntario import views

urlpatterns = [
    path('', views.index, name='euamovida-seja-voluntario'),
]
