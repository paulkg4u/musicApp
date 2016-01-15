from django.db import models
from django.contrib.auth.models import User
from userprofile.models import UserProfile


def image_path(instance,filename):
	return 'userpics'+str(instance.fileOwner.userObject.username)+str(instance.id)

class AudioFile(models.Model):
	fileOwner = models.ForeignKey(UserProfile)
	fileDescription = models.TextField(default = "",null  = True, blank  = True)
	audioFile = models.FileField(upload_to = image_path)
	slugText = models.SlugField(max_length = 100, null = True, blank = True)
	def __unicode__(self):
		return unicode(self.id)
