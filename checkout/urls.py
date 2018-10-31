from django.urls import path
from checkout import views

urlpatterns = [
    path('carrinho/<int:produto_id>', views.create_cartitem, name='create_cartitem'),
    path('carrinho/', views.cart_item, name='cart_item'),
    path('carrinho/', views.index, name='euamovida-carrinho'),
]
