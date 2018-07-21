from django import forms

class GenForm(forms.Form):
	msg = forms.CharField(label='Message:',widget=forms.Textarea)
	font_size = forms.IntegerField(label='Font size(12-80):',min_value=12,max_value=80)
	x = forms.IntegerField(label='X(0-50):',min_value=0,max_value=50)
	y = forms.IntegerField(label='Y(0-100):',min_value=0,max_value=100)