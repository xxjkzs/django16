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
# Create your views here.

def index(request):
	# send_mail("Someone visted your site.","FYI","service@mysite.org",["xxjkzs@foxmail.com"])
	messages.get_messages(request)
	template = get_template('index.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)

	return HttpResponse(html)