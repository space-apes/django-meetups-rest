from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime

# Create your models here.

#set up a custom user model that can be extended AND used in auth
#dont forget to update AUTH_USER_MODEL to settings.py
#dont forget to add this model to admin.py

class User(AbstractUser):
	#wow! avoided circular dependency by specifying model as string. cool. 

	def __str__(self):
		return self.username	

class MeetupGroup(models.Model):
	name = models.CharField(max_length=25)
	description = models.CharField(max_length=100, default='default description')
	create_date = models.DateField('date created')
	members = models.ManyToManyField(User)
	admin = models.ForeignKey(User, null = True, related_name="admin_user", on_delete=models.CASCADE)
		

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=25)
	create_date = models.DateField('date created')
	meetup_groups = models.ManyToManyField(MeetupGroup)

	def __str__(self):
		return self.name

class Event(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	date = models.DateTimeField('date of event')
	address = models.CharField(max_length = 100)
	date_created = models.DateField('date created')
	host = models.ForeignKey(User, related_name='host_user', on_delete=models.CASCADE)
	meetup_group = models.ForeignKey(MeetupGroup, on_delete=models.CASCADE)
	participants = models.ManyToManyField(User)
	
	def __str__(self):
		return self.name