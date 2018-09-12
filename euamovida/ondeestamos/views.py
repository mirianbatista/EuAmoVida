from django.shortcuts import render

def index(request):
	return render(request, 'ondeestamos/ondeestamos.html')