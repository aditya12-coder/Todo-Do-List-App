from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class todo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.TextField()
	date= models.DateField(auto_now_add=True)
	is_completed_choice = (('Yes', 'Yes'), ('No', 'No'))
	is_completed = models.CharField(max_length=3, choices=is_completed_choice, default='No')
	
	def __str__(self):
		return self.user.username + " : " +  self.title