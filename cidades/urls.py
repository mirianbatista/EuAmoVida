from django.urls import path
from .views import lista_cidades, exibir_cidade, cidades


urlpatterns = [
path('', cidades, name ='euamovida-cidades'),
path('cidade/<int:cidade_id>', exibir_cidade, name='euamovida-cidade')

]
