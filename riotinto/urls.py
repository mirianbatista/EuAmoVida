from django.urls import path
from riotinto import views

urlpatterns = [
    path('', views.index, name='euamovida-rio-tinto'),
]
