from django.shortcuts import render

def index(request):
	return render(request, 'baia_marcacao/baia-marcacao.html')