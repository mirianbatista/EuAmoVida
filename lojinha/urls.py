from django.urls import path
from .views import lista_produtos, exibir_produto

urlpatterns = [
path('', lista_produtos, name = 'euamovida-lojinha'),
path('produto/<int:produto_id>', exibir_produto, name='euamovida-produto')

]
