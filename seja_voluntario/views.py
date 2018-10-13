from django.shortcuts import render

def index(request):
	return render(request, 'seja_voluntario/seja-voluntario.html')