from django.urls import path
from colabore import views

urlpatterns = [
    path('', views.index),
]
