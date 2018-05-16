from django.shortcuts import render
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import EmailMessage
from mysite import models,forms
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
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)
	return HttpResponse(html)

def contact(request):
	if request.method == 'POST':
		form = forms.ContactForm(request.POST)
		if form.is_valid():
			message = 'Thanks for your suggestion.'
			user_name = form.cleaned_data['user_name']
			user_city = form.cleaned_data['user_city']
			user_school = form.cleaned_data['user_school']
			user_email = form.cleaned_data['user_email']
			user_message = form.cleaned_data['user_message']
			mail_body = u'''
			From:{}
			Citt:{}
			In School:{}
			Suggestion:{}'''.format(user_name,user_city,user_school,user_message)
			email = EmailMessage('New message:',
				mail_body,
				user_email,
				['xxjkzs@foxmail.com'])
			email.send()
		else:
			message = 'Please check your input.'
	else:
		form = forms.ContactForm
	template = get_template('contact.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)
	return HttpResponse(html)


def post2db(request):
	if request.method == 'POST':
		post_form = forms.PostForm(request.POST)
		if post_form.is_valid():
			message = "Your message saved."
			post_form.save()
			return HttpResponseRedirect('/list/')
		else:
			message = "All fields must be filled in."
	else:
		post_form = forms.PostForm()
		message = "All fields must be filled in."
	template = get_template('post2db.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)
	return HttpResponse(html)
