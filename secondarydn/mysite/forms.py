from django.forms import ModelForm
from mysite import models

class SubDomainForm(ModelForm):
	class Meta:
		model = models.SubDomain
		fields = ['name']

	def __init__(self,*args,**kwargs):
		super(SubDomainForm,self).__init__(*args,**kwargs)
		self.fields['name'].label='Site ID'