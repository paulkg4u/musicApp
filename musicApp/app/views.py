from django.shortcuts import render
from django.http import HttpResponseRedirect
def home(request):
	if request.user != 'AnonymousUser':
		return HttpResponseRedirect('/accounts/login/')
	contextDi = {}
	return render(request,'musicApp/home.html',contextDi)
