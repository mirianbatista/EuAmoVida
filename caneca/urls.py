from django.urls import path
from caneca import views

urlpatterns = [
    path('', views.index, name='euamovida-caneca'),
]
