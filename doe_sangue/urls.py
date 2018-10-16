from django.urls import path
from doe_sangue import views

urlpatterns = [
    path('', views.index, name='euamovida-doe-sangue'),
]
