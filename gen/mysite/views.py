from django.shortcuts import render
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
import os,random
from PIL import Image, ImageDraw, ImageFont
from uuid_upload_path import uuid
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


def gen(request):
	messages.get_messages(request)

	if request.method == 'POST':
		form = forms.GenForm(request.POST)
		if form.is_valid():
			saved_filename = merge_pic(request.POST.get('msg'),
				int(request.POST.get('font_size')),
				int(request.POST.get('x')),
				int(request.POST.get('y'))
				)
	else:
		form = forms.GenForm()

	template = get_template('gen.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)

	return HttpResponse(html)


def merge_pic(msg,font_size,x,y):
	fill = (0,0,0,255)
	image_file = Image.open(os.path.join(settings.BASE_DIR,'static/backimages/back1.jpg'))
	im_w, im_h = image_file.size
	im0 = Image.new('RGBA',(1,1))
	dw0 = ImageDraw.Draw(im0)
	font = ImageFont.truetype(os.path.join(settings.BASE_DIR,'stocky.ttf'),font_size)
	fn_w, fn_h = dw0.textsize(msg,font=font)

	im = Image.new('RGBA',(fn_w,fn_h),(255,0,0,0))
	dw = ImageDraw.Draw(im)
	dw.text((0,0),msg,font=font,fill=fill)
	image_file.paste(im,(x,y),im)
	saved_filename = uuid()+'.jpg'
	image_file.save(os.path.join(settings.BASE_DIR,"media",saved_filename))
	return saved_filename