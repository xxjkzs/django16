from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SubDomain(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
		