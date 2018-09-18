from django.urls import path
from campanha2019 import views

urlpatterns = [
    path('', views.index, name='euamovida-campanha2019'),
]
