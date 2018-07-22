from django.shortcuts import render
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os,random,glob
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
	backfiles = glob.glob(os.path.join(settings.BASE_DIR,'static/backimages/*.jpg'))
	if request.method == 'POST':
		form = forms.GenForm(request.POST)
		back_file = os.path.join(settings.BASE_DIR,
            'static/backimages/', 
            request.POST.get('backfile'))

		saved_filename = merge_pic(back_file,
			request.POST.get('msg'),
			int(request.POST.get('font_size')),
			int(request.POST.get('x')),
			int(request.POST.get('y'))
			)
	else:
		form = forms.GenForm(backfiles)

	template = get_template('gen.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)

	return HttpResponse(html)


def merge_pic(image_file,msg,font_size,x,y):
	fill = (0,0,0,255)
	try:
		image_file = Image.open(image_file)
	except:
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


@login_required
def vip(request):
	messages.get_messages(request)
	custom_backfile = None
	if 'custom_backfile' in request.session:
		if len(request.session.get('custom_backfile')) > 0:
			custom_backfile = request.session.get('custom_backfile')

	if request.method == 'POST':
		if 'change_backfile' in request.POST:
			upload_form = forms.UploadForm(request.POST,request.FILES)
			if upload_form.is_valid():
				custom_backfile = save_backfile(request.FILES['file'])
				request.session['custom_backfile'] = custom_backfile
				messages.add_message(request,messages.SUCCESS,"Upload done!")
				return redirect('/vip/')
			else:
				messages.add_message(request,messages.WARNING,"Upload failed!")
				return redirect('/vip/')
		else:
			form = forms.CustomForm(request.POST)
			if custom_backfile is None: 
				back_file = os.path.join(settings.BASE_DIR,'static/backimages/back1.jpg')
			else:
				back_file = os.path.join(settings.BASE_DIR,'media',custom_backfile)

			saved_filename = merge_pic(back_file,
			request.POST.get('msg'),
			int(request.POST.get('font_size')),
			int(request.POST.get('x')),
			int(request.POST.get('y'))
			)
	else:
		form = forms.CustomForm()
		upload_form = forms.UploadForm()

	template = get_template('vip.html')
	request_context = RequestContext(request)
	request_context.push(locals())
	html = template.render(request_context)

	return HttpResponse(html)

def save_backfile(f):
	target = os.path.join(settings.BASE_DIR,'media',uuid()+'.jpg')
	with open(target,'wb') as des:
		for chunck in f.chunks():
			des.write(chunck)
	return os.path.basename(target)