from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Colabore

class ColaboreListView(generic.ListView):
	model = Colabore
	template_name = 'colabore/colabore.html'
	context_object_name = 'doacoes'
	paginate_by = 3

colabore = ColaboreListView.as_view()

def lista_doacoes(request):
    doacoes = Colabore.objects.all()
    return render(request, 'colabore/colabore.html', {'doacoes' : doacoes})

def exibir_doacao(request, doacao_id):
	doacao = Colabore.objects.get(pk=doacao_id)
	return render(request, 'colabore/doacao.html', {'doacao': doacao})