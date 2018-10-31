from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Cidade

class CidadeListView(generic.ListView):
	model = Cidade
	template_name = 'cidades/cidades.html'
	context_object_name = 'cidades'
	paginate_by = 3

cidades = CidadeListView.as_view()

def lista_cidades(request):
    cidades = Cidade.objects.all()
    return render(request, 'cidades/cidades.html', {'cidades' : cidades})

def exibir_cidade(request, cidade_id):
	cidade = Cidade.objects.get(pk=cidade_id)
	return render(request, 'cidades/cidade.html', {'cidade': cidade})