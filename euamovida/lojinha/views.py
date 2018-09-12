from django.shortcuts import render

def index(request):
	context_dict = {'nome_do_produto': "Camisa 2019"}

	return render(request, 'lojinha/loja.html', context=context_dict)