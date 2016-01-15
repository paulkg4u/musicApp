from django.shortcuts import render
from django.http import HttpResponseRedirect
from pydub import AudioSegment
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from .models import AudioFile
def home(request):
	if str(request.user) == 'AnonymousUser':
		return HttpResponseRedirect('/accounts/login/')
	contextDi = {}
	return render(request,'musicApp/home.html',contextDi)

def uploadFile(request):
	if request.POST:
		contextDi = {}
		if request.FILES:
			username = request.user
			userProfile = UserProfile.objects.get(userObject = User.objects.get(username = username))
			fileDescription = request.POST['fileDescription']
			uploadedFile = request.FILES['mp3File']
			fileUploaded = AudioFile.objects.create(fileOwner = userProfile,fileDescription=fileDescription,audioFile = uploadedFile)
			newURL = fileUploaded.audioFile.url[1:]
			actualFile = AudioSegment.from_mp3(newURL)
			actualFile.export(newURL,format="mp3",bitrate="128K")
			print "success"
			
	return HttpResponseRedirect('/app/')