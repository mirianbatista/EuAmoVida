from django.urls import path
from doe_alimentos import views

urlpatterns = [
    path('', views.index, name='euamovida-doe-alimentos'),
]
