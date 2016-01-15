from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def viewUser(request,userName):
	contextDi = {}
	return render(request,'musicApp/userProfile.html',contextDi)

@login_required
def logout_view(request):
	logout(request)
	print "logged out"
	return HttpResponseRedirect('/app/')
