from django.urls import path
from ondeestamos import views

urlpatterns = [
    path('', views.index),
]
