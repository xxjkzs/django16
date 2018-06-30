from django import forms
# from captcha.fields import CaptchaField
from django.forms import ModelForm
from mysite import models

class PollForm(ModelForm):
    class Meta:
        model = models.Poll
        fields = ['name', 'enabled']
    def __init__(self, *args, **kwargs):
        super(PollForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Title'
        self.fields['enabled'].label = 'Enable'

class PollItemForm(ModelForm):
    class Meta:
        model = models.PollItem
        fields = ['name', 'image_url', 'vote']
    def __init__(self, *args, **kwargs):
        super(PollItemForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Item Name'
        self.fields['image_url'].label = 'Image URL'
        self.fields['vote'].label = 'Vote(s)'