from django import forms
from captcha.fields import CaptchaField
from mysite import models

class ContactForm(forms.Form):
	CITY = [
		['DL','Dali'],
		['DG','Dongguan'],
		['ZB','Zibo'],
		['FD','Fuding'],
		['SZ','Suzhou'],
		['NC','NanChang'],
		['NA','Other']
	]
	user_name = forms.CharField(label='Your Name:',max_length=50,initial='Thanos')
	user_city = forms.ChoiceField(label='Living City:',choices=CITY)
	user_school = forms.BooleanField(label='In School?',required=False)
	user_email = forms.EmailField(label='Email Address:')
	user_message = forms.CharField(label='Your suggestion:',widget=forms.Textarea)


class PostForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = models.Post
		fields = ['mood','nickname','message','del_pass']
	def __init__(self,*args,**kwargs):
		super(PostForm,self).__init__(*args,**kwargs)
		self.fields['mood'].label='Mood'
		self.fields['nickname'].label='Nickname'
		self.fields['message'].label='Message'
		self.fields['del_pass'].label='Password'


class LoginForm(forms.Form):
	username = forms.CharField(label='Your name',max_length=10)
	password = forms.CharField(label='Password',widget=forms.PasswordInput())


class DateInput(forms.DateInput):
	input_type = 'date'


class DiaryForm(forms.ModelForm):

	class Meta:
		model = models.Diary
		# fields = ['user','budget','weight','note','ddate']
		fields = ['budget','weight','note','ddate']
		widgets = {
			'ddate':DateInput(),
		}

		def __init__(self,*args,**kwargs):
			super(DiaryForm,self).init(*args,**kwargs)
			# self.fields['user'].label='User'
			self.fields['budget'].label='Expenses'
			self.fields['weight'].label='Weight'
			self.fields['note'].label='Notes'
			self.fields['ddate'].label='Date'


class ProfileForm(forms.ModelForm):
	class Meta:
		model = models.Profile
		fields = ['height','male','website']

	def __init__(self,*args,**kwargs):
		super (ProfileForm,self).__init__(*args,**kwargs)
		self.fields['height'].label='Height(cm)'
		self.fields['male'].label='Male?'
		self.fields['website'].label='Website'