from django import forms
# from captcha.fields import CaptchaField
from django.forms import ModelForm
from mysite import models

class OrderForm(forms.ModelForm):
	class Meta:
		model = models.Order
		fields = ['full_name','address','phone']
	def __init__(self,*args,**kwargs):
		super(OrderForm,self).__init__(*args,**kwargs)
		self.fields['full_name'].label='Receipient'
		self.fields['address'].label='Address'
		self.fields['phone'].label='Contact'