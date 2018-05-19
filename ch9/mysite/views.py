from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import EmailMessage
from django.contrib import messages , auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from mysite import models,forms
# Create your views here.

def index(request,pid=None,del_pass=None):
	if request.user.is_authenticated():
		username = request.user.username
	messages.get_messages(request)
	template = get_template('index.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)
	return HttpResponse(html)

def login(request):
	if request.method == 'POST':
		login_form = forms.LoginForm(request.POST)
		if login_form.is_valid():
			login_name = request.POST['username'].strip()
			login_pass = request.POST['password']
			user = authenticate(username=login_name,password=login_pass)
			if user is not None:
				if user.is_active:
					auth.login(request,user)
					print("Successs!")
					messages.add_message(request,messages.SUCCESS,'Logged in.')
					return redirect('/')
				else:
					messages.add_message(request,messages.WARNING,'User is not activated.')
			else:
				messages.add_message(request,messages.WARNING,'Login failed.')
		else:
			messages.add_message(request,messages.INFO,'Check your input.')
	else:
		login_form = forms.LoginForm()

	template = get_template("login.html")
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)
	response = HttpResponse(html)
	return response

def logout(request):
	auth.logout(request)
	messages.add_message(request,messages.INFO,'Logged out.')
	return redirect('/')


@ login_required(login_url='/login/')
def profile(request):
	if request.user.is_authenticated():
		username = request.user.username
		email = request.user.email
		firstname = request.user.first_name
		lastname = request.user.last_name
	try:
		profile = User.objects.get(username='username')
	except:
		pass
	template = get_template('profile.html')
	html = template.render(locals())
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
