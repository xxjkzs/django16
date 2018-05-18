from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import EmailMessage
from mysite import models,forms
# Create your views here.

def index(request,pid=None,del_pass=None):
	if 'username' in request.session:
		username = request.session['username']
		useremail = request.session['useremail']
	template = get_template('index.html')
	html = template.render(locals())
	return HttpResponse(html)

def login(request):
	if request.method == 'POST':
		login_form = forms.LoginForm(request.POST)
		if login_form.is_valid():
			login_name = request.POST['username'].strip()
			login_pass = request.POST['password']
			try:
				user = models.User.objects.get(name=login_name)
				if user.password == login_pass:
					response = redirect('/')
					request.session['username'] = user.name
					request.session['useremail'] = user.email
					return response
				else:
					message = "Invalid Password."
			except:
				message = "Cannot login now."
		else:
			message = "Check your input."
	else:
		login_form = forms.LoginForm()

	template = get_template("login.html")
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)
	response = HttpResponse(html)
	return response

def logout(request):
	response = HttpResponseRedirect('/')
	response.delete_cookie('username')
	return response


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
