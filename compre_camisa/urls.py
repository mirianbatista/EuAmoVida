from django.urls import path
from compre_camisa import views

urlpatterns = [
    path('', views.index, name='euamovida-compre-camisa'),
]
