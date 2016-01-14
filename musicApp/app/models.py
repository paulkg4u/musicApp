from django.db import models
from django.contrib.auth.models import User
from userprofile.models import UserProfile

class AudioFile(models.Model):
	fileOwner = models.ForeignKey(UserProfile)
	fileDescription = models.TextField(default = "",null  = True, blank  = True)
	audioFile = models.FileField(upload_to = "files/")
	slugText = models.SlugField(max_length = 100, null = True, blank = True)
	def __unicode__(self):
		return unicode(self.id)
