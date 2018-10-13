from django.urls import path
from cg import views

urlpatterns = [
    path('', views.index, name='euamovida-doe-sangue'),
]
