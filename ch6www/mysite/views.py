from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
	template = get_template('index.html')
	now = datetime.now()
	html = template.render(locals())
	return HttpResponse(html)