from django.urls import path
from lojinha import views

urlpatterns = [
    path('', views.index),
]
