from django.urls import path
from caneta import views

urlpatterns = [
    path('', views.index, name='euamovida-caneta'),
]
