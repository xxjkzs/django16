from django.db import models

# Create your models here.
class Mood(models.Model):
	status = models.CharField(max_length=10,null=False)

	def __str__(self):
		return self.status

class Post(models.Model):
	mood = models.ForeignKey('Mood',on_delete=models.CASCADE)
	nickname = models.CharField(max_length=10,default='Anonymous')
	message = models.TextField(null=False)
	del_pass = models.CharField(max_length=10)
	pub_time = models.DateTimeField(auto_now=True)
	enabled = models.BooleanField(default=True)

	def __str__(self):
		return self.message