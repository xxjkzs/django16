from django.shortcuts import render
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
from dnsimple import DNSimple
from mysite import models,forms
from django.conf import settings
# Create your views here.

def index(request):
	messages.get_messages(request)

	pics = random.sample(range(1,87),6)

	template = get_template('index.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)

	return HttpResponse(html)
