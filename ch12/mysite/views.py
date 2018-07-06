from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
# from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
# from allauth.account.decorators import verified_email_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import datetime
from mysite import models,forms

# Create your views here.
def index(request):
    all_products = models.Product.objects.all()
    paginator = Paginator(all_products,5)
    p = request.GET.get('p')
    try:
        products = paginator.page(p)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    template = get_template('index.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)