from django.urls import path
from mamanguape import views

urlpatterns = [
    path('', views.index, name='euamovida-mamanguape'),
]
