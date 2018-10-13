from django.shortcuts import render

def index(request):
	return render(request, 'doe_sangue/doe-sangue.html')