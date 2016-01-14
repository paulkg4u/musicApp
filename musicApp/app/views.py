from django.shortcuts import render

def home(request):
	contextDi = {}
	return render(request,'musicApp/home.html',contextDi)
