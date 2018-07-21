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
	if len(subdomains) > 0:
		records_in_dnsimple = subdomain_in_dnsimple(subdomains[0].name)
		main_subdomain = subdomains[0].name

	if request.method == 'POST':
		user = User.objects.get(username=request.user.username)
		new_subdomain = models.SubDomain(user=user)
		form = forms.SubDomainForm(request.POST,instance=new_subdomain)
		if form.is_valid():
			cleaned_info = form.cleaned_data
			if models.SubDomain.objects.filter(name=cleaned_info['name']).exists():
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
	messages.get_messages(request)
	try:
		target = models.SubDomain.objects.get(user=request.user,name=subdomain)
		target.delete()
		dns = DNSimple(email=settings.DNSIMPLE_USERNAME,password=settings.DNSIMPLE_PASSWORD)
		records_in_dnsimple = subdomain_in_dnsimple(subdomain)
		for rec in records_in_dnsimple():
			try:
				dns.delete_record('locahost:8000',rec['id'])
			except:
				messages.add_message(request,messages.WARNING,"Failed to connect with DNSimple")
				pass
		messages.add_message(request,messages.SUCCESS,"Deleted all records.")
	except:
		messages.add_message(request,messages.WARNING,"Failed to delete records.")
		pass
	return redirect('/dnsmanager')


@login_required
def del_record(request,subdomain):
	messages.get_messages(request)
	try:
		dns = DNSimple(email=settings.DNSIMPLE_USERNAME,password=settings.DNSIMPLE_PASSWORD)
		dns.delete_record('badmonkeybars.top',rec_id)
		messages.add_message(request,messages.SUCCESS,"Deleted!")
	except:
		messages.add_message(request,messages.WARNING,"Failed!")
		pass
	return redirect('/dnsmanager')


@login_required
def add_record(request,subdomain):
	messages.get_messages(request)
	if request.method == 'POST':
		content = request.POST.get('content')
		record_type = request.POST.get('record_type')
		try:
			dns = DNSimple(email=settings.DNSIMPLE_USERNAME,password=settings.DNSIMPLE_PASSWORD)
			dns.add_record('badmonkeybars.top',{ 'name':subdomain,
				'record_type':record_type,
				'content':content})
			messages.add_message(request,messages.SUCCESS,"Added!")
		except:
			messages.add_message(request,messages.WARNING,"Failed!")
			pass
	return redirect('/dnsmanager')


def subdomain_in_dnsimple(subdomain):
	dns = DNSimple(email=settings.DNSIMPLE_USERNAME,password=settings.DNSIMPLE_PASSWORD)
	try:
		mysite_records = dns.records('badmonkeybars.top')
	except:
		return None
	mysite_dns_records = list()
	for mysite_record in mysite_records:
		if mysite_record['record']['name'] == subdomain:
			t = dict()
			t['id'] = mysite_record['record']['id']
			t['name'] = mysite_record['record']['name']
			t['type'] = mysite_record['record']['type']
			t['content'] = mysite_record['record']['content']
			mysite_dns_records.append(t)
	return mysite_dns_records