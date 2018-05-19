from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import EmailMessage
from django.contrib import messages , auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from mysite import models,forms
# Create your views here.

def index(request,pid=None,del_pass=None):
	if request.user.is_authenticated():
		username = request.user.username
		useremail = request.user.email
		try:
			user = models.User.objects.get(username=username)
			diaries = models.Diary.objects.filter(user=user).order_by('-ddate')
		except:
			pass
	
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
	user = User.objects.get(username=username)
	try:
		profile = models.Profile.objects.get(user=user)
	except:
		profile = models.Profile(user=user)
	if request.method == 'POST':
		profile_form = forms.ProfileForm(request.POST,instance=profile)
		if profile_form.is_valid():
			messages.add_message(request,messages.INFO,'Profile updated.')
			profile_form.save()
			return redirect('/')
		else:
			messages.add_message(request,messages.INFO,'All fields must be modified.')
	else:
		profile_form = forms.ProfileForm()

	template = get_template('profile.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)
	return HttpResponse(html)


@ login_required(login_url='/login/')
def write(request):
	if request.user.is_authenticated():
		username = request.user.username
		useremail = request.user.email
	messages.get_messages(request)

	if request.method == 'POST':
		user = User.objects.get(username=username)
		diary = models.Diary(user=user)
		post_form = forms.DiaryForm(request.POST,instance=diary)
		if post_form.is_valid():
			messages.add_message(request,messages.INFO,'Saved')
			post_form.save()
			return redirect('/')
		else:
			messages.add_message(request,messages.INFO,'All fields must be filled.')
	else:
		post_form = forms.DiaryForm()
		messages.add_message(request,messages.INFO,'All fiels must be filled.')

	template = get_template('write.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)
	return HttpResponse(html)
