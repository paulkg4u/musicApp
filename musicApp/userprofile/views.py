from django.shortcuts import render


def viewUser(request,userName):
	contextDi = {}
	return render(request,'musicApp/userProfile.html',contextDi)