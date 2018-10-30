from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Produto

class ProductListView(generic.ListView):
	model = Produto
	template_name = 'lojinha/loja.html'
	context_object_name = 'produtos'
	paginate_by = 3

loja = ProductListView.as_view()

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lojinha/loja.html', {'produtos' : produtos})

def exibir_produto(request, produto_id):
	produto = Produto.objects.get(pk=produto_id)
	return render(request, 'lojinha/produto.html', {'produto': produto})