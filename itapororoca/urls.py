from django.urls import path
from itapororoca import views

urlpatterns = [
    path('', views.index, name='euamovida-itapororoca'),
]
