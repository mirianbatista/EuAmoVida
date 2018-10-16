from django.urls import path
from camisa import views

urlpatterns = [
    path('', views.index, name='euamovida-camisa'),
]
