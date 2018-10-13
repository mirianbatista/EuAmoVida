from django.shortcuts import render

def index(request):
	return render(request, 'riotinto/rio-tinto.html')