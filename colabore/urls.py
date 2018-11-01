from django.urls import path
from .views import lista_doacoes, exibir_doacao, colabore


urlpatterns = [
path('', colabore, name = 'euamovida-colabore'),
path('doacao/<int:doacao_id>', exibir_doacao, name='euamovida-doacao')

]
