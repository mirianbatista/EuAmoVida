from django.urls import path
from copo import views

urlpatterns = [
    path('', views.index, name='euamovida-copo'),
]
