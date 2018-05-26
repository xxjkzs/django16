from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Poll(models.Model):
    name = models.CharField(max_length=200,null=False)
    created_at = models.DateField(auto_now_add=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PollItem(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=False)
    image_url = models.CharField(max_length=200,null=True,blank=True)
    vote = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name