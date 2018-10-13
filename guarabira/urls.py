from django.urls import path
from guarabira import views

urlpatterns = [
    path('', views.index, name='euamovida-guarabira'),
]
