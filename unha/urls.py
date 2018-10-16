from django.urls import path
from unha import views

urlpatterns = [
    path('', views.index, name='euamovida-unha'),
]
