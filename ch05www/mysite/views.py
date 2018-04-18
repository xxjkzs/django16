from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template.loader import get_template
from django.core.urlresolvers import reverse

# Create your views here.
def homepage(request):
	template = get_template('homepage.html')
	html = template.render()
	return HttpResponse(html)

# def about(request):
def about(request,author_no):
	html = "<h2>Author:{}</h2><hr>".format(author_no)
	# html = "<h2>Author:N</h2><hr>"
	return HttpResponse(html)

def listing(request,list_date):
	html = "<h2>List date is {}</h2><hr>".format(list_date)
	return HttpResponse(html)

def post(request,yr,mon,day,post_no):
	# html = "<h2>Post data is {}</h2><hr>".format(post_data)
	html = "<h2>Post date is {}年{}月{}日，post number is {}</h2><hr>".format(yr,mon,day,int(post_no))

	return HttpResponse(html)

def home(request,year,month,day,postid):
	year = 2019
	month = 12
	day = 9
	postid = 11
	template = get_template('index.html')
	html = template.render()
	# html = "<a href='{}'>Show the post</a>".format(reverse('post-url',args = (year,month,day,postid,)))
	return HttpResponse(html)