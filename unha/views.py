from django.shortcuts import render

def index(request):
	return render(request, 'unha/unha.html')