from django.db import models
from django.contrib.auth.models import User
from userprofile.models import UserProfile
import random


def image_path(instance,filename):
	return 'files/'+str(instance.fileOwner.userObject.username)+str(int(random.random()*100000))+'.mp3'

class AudioFile(models.Model):
	fileOwner = models.ForeignKey(UserProfile)
	fileTitle = models.CharField(max_length = "200",default = "MP3 File")
	fileDescription = models.TextField(default = "",null  = True, blank  = True)
	audioFile = models.FileField(upload_to = image_path)
	slugText = models.SlugField(max_length = 100, null = True, blank = True)
	def __unicode__(self):
		return unicode(self.fileDescription)
