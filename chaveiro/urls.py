from django.urls import path
from chaveiro import views

urlpatterns = [
    path('', views.index, name='euamovida-chaveiro'),
]
