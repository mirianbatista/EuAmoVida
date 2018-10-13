from django.urls import path
from jacarau import views

urlpatterns = [
    path('', views.index, name='euamovida-jacarau'),
]
