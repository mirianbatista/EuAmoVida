from django.urls import path
from doe_cereais import views

urlpatterns = [
    path('', views.index, name='euamovida-doe-cereais'),
]
