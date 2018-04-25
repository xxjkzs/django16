from django.db import models

# Create your models here.
class Maker(models.Model):
	name = models.CharField(max_length=10)
	country = models.CharField(max_length=10)

	# def __unicode__(self):
	def __str__(self):
		return self.name

class PModel(models.Model):
	maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	url = models.URLField(default='http://i.imgur.com/Ous4iGB.png')

	# def __unicode__(self):
	def __str__(self):
		return self.name

class Product(models.Model):
	pmodel = models.ForeignKey(PModel,on_delete=models.CASCADE,verbose_name='型号')
	nickname = models.CharField(max_length=15,default='Great Value Secondhand Phones',verbose_name='摘要' )
	discription = models.TextField(default='N/A')
	year = models.PositiveIntegerField(default=2018)
	price = models.PositiveIntegerField(default=0)

	# def __unicode__(self):
	def __str__(self):
		return self.nickname

class PPhoto(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	discription = models.CharField(max_length=20,default='Product Photo')
	url = models.URLField(default='http://i.imgur.com/Z230eeq.png')

	# def __unicode__(self):
	def __str__(self):
		return self.discription

		