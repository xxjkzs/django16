from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from mysite import models
# Create your views here.

def index(request):
	years = range(1960,2020)
	ufcolor = request.GET.getlist('fcolor')
	template = get_template('index.html')
	posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
	moods = models.Mood.objects.all()
	try:
		uid = request.GET['user_id']
		upass = request.GET['user_pass']
	except:
		uid = None
	if uid != None and upass == '123456':
		verified = True
	else:
		verified = False
	html = template.render(locals())
	return HttpResponse(html)