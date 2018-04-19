from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
# def index(request):
# 	template = get_template('index.html')
# 	now = datetime.now()
# 	html = template.render(locals())
# 	return HttpResponse(html)

def index(request,tvno='0'):
	tv_list = [{'name':'GOKURAKU JODO','tvcode':'aid=6449135&cid=10486949&page=1'},
				{'name':'Oeasy','tvcode':'aid=1290353&cid=1961804&page=9'},]

	template = get_template('index.html')
	now = datetime.now()
	tvno = tvno
	tv = tv_list[int(tvno)]
	html = template.render(locals())
	return HttpResponse(html)