from django.urls import path
from checkout import views

urlpatterns = [
    path('carrinho/<int:produto_id>', views.create_cartitem, name='create_cartitem'),
]
