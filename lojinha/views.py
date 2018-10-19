from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lojinha/loja.html', {'produtos' : produtos})

def exibir_produto(request, produto_id):
	produto = Produto.objects.get(pk=produto_id)
	return render(request, 'lojinha/produto.html', {'produto': produto})