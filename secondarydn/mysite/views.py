from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from mysite import models,forms
# Create your views here.

def index(request):
	# send_mail("Someone visted your site.","FYI","service@mysite.org",["xxjkzs@foxmail.com"])
	messages.get_messages(request)
	template = get_template('index.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)

	return HttpResponse(html)


@login_required
def dnsmanager(request):
	messages.get_messages(request)
	subdomains = models.SubDomain.objects.filter(user=request.user)
	if request.method == 'POST':
		user = User.objects.get(username=request.user.username)
		new_subdomain = models.SubDomain(user=user)
		form = forms.SubDomainForm(request.POST,instance=new_subdomain)
		if form.is_valid():
			cleaned_info = form.cleaned_data
			if models.SubDomain.objects.filter(name=cleaned_info['name'].exists()):
				messages.add_message(request,messages.WARNING,"this domain name is already rigisterred")
				return redirect('/dnsmanager')
			else:
				form.save()
				return redirect('/dnsmanager')
		else:
			form = forms.SubDomainForm()

	template = get_template('dnsmanager.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)

	return HttpResponse(html)


@login_required
def del_subdomain(request,subdomain):
	try:
		target = models.SubDomain.objects.get(user=request.user,name=subdomain)
		target.delete()
	except:
		pass
	return redirect('/dnsmanager')