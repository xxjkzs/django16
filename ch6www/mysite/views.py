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
	hour = now.timetuple().tm_hour
	tvno = tvno
	tv = tv_list[int(tvno)]
	html = template.render(locals())
	return HttpResponse(html)

def othertv(request,tvno='0'):
	tv_list = [{'name':'HEROS3','tvcode':'aid=431527&cid=658069&page=1'},
				{'name':'DISCOVERY','tvcode':'aid=2644473&cid=4128935&page=6'},]
	template = get_template('other.html')
	now = datetime.now()
	tvno = tvno
	tv = tv_list[int(tvno)]
	html = template.render(locals())
	return HttpResponse(html)

def carlist(request,maker = 0):
	car_maker = ['SAAB','Ford','Honda','Mazda','Nissan','Toyota']
	carlist = [ [],
	['Fiesta','Foucus','Modeo','EcoSport','Kuga','Mustang'],
	['Fit','Odessy','CR-V','City','NSX'],
	['Mazda3','Mazda5','Mazda6','CX-3','CX-5','MX-5'],
	['Tida','March','Livina','Sentra','Teana','X-Trail','Juke','Murano'],
	['Camary','Altis','Yaris','86','Prius','Vios','RAV4','Wish']
	]
	maker = int(maker)
	maker_name = car_maker[maker]
	cars = carlist[maker]
	template = get_template('carlist.html')
	html = template.render(locals())
	return HttpResponse(html)

def carprice(request,maker = 0):
	car_maker = ['Ford','Honda','Mazda']
	carlist = [ 
		[{'model':'Fiesta','price':203500},
		{'model':'Foucus','price':650000},
		{'model':'Modeo','price':900000}],
		[[{'model':'Fit','price':450000},
		{'model':'City','price':150000},
		{'model':'NSX','price':1200000}],],
		[[{'model':'Mazda3','price':329999},
		{'model':'Mazda5','price':605000},
		{'model':'Mazda6','price':850000}],]
	]
	maker = int(maker)
	maker_name = car_maker[maker]
	cars = carlist[maker]
	template = get_template('carprice.html')
	html = template.render(locals())
	return HttpResponse(html)