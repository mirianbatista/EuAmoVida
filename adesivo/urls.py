from django.urls import path
from adesivo import views

urlpatterns = [
    path('', views.index, name='euamovida-adesivo'),
]
