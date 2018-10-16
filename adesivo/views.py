from django.shortcuts import render

def index(request):
	return render(request, 'adesivo/adesivo.html')