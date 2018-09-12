from django.shortcuts import render

def index(request):
	return render(request, 'campanha2019/campanha2019.html')