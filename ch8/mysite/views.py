from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from mysite import models
# Create your views here.

def index(request,pid=None,del_pass=None):
	template = get_template('index.html')
	posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
	moods = models.Mood.objects.all()
	try:
		uid = request.GET['user_id']
		upass = request.GET['user_pass']
		upost = request.GET['user_post']
		umood = request.GET['mood']
	except:
		uid = None
		message = 'All forms need to be filled in.'
	if del_pass and pid:
		try:
			post = models.Post.objects.get(id=pid)
		except:
			post = None
		if post:
			if post.del_pass == del_pass:
				post.delete()
				message = 'Deleted'
			else:
				message = 'Wrong Password'
	elif uid != None :
		mood = models.Mood.objects.get(status=umood)
		post = models.Post.objects.create(mood=mood,nickname=uid,del_pass=upass,message=upost)
		post.save
		message = 'Post saved, please remember your editting password [{}] '.format(upass)
	html = template.render(locals())
	return HttpResponse(html)

def listing(request):
	template = get_template("list.html")
	posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
	moods = models.Mood.objects.all()
	html = template.render(locals())
	return HttpResponse(html)

def posting(request):
	template = get_template("post.html")
	moods = models.Mood.objects.all()
	message = "All fields need to be filled  for a new post."
	html = template.render(locals())
	return HttpResponse(html)