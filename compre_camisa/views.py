from django.shortcuts import render

def index(request):
	return render(request, 'compre_camisa/compre-camisa.html')