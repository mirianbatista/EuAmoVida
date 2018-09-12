from django.urls import path
from sobre import views

urlpatterns = [
    path('', views.index),
]
