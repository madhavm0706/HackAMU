from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
	is_user   = models.BooleanField(default=False)
	is_police = models.BooleanField(default=False)

class UserUpdate(models.Model):
	user 		= models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	f_name   	= models.CharField(max_length=20,blank=False)
	l_name		= models.CharField(max_length=20,blank=False)
	city  		= models.CharField(max_length=40,blank=False)
	phone 		= models.CharField(max_length=10,blank=False)
	address		= models.TextField()

	def __str__(self):
		return self.user.username


class Donation_list(models.Model):

    

    items= models.TextField()

	
       