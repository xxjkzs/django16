from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(null=True)
    website = models.URLField(null=True)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return self.name
