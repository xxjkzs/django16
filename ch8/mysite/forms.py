from django import forms

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