from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	userObject = models.OneToOneField(User)
	firstName = models.CharField(max_length = "200")
	lastName = models.CharField(max_length = "200")
	profilePicture = models.ImageField(upload_to = 'userpics/',blank = True)
	def __unicode__(self):
		return unicode(userObject)
