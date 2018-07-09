from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
# from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
# from allauth.account.decorators import verified_email_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from cart.cart import Cart
import datetime
from mysite import models,forms

# Create your views here.
def index(request,cat_id=0):
    all_categories = models.Category.objects.all()
    all_products = None
    if int(cat_id) > 0:
        try:
            category = models.Category.objects.get(id=cat_id)
        except:
            category = None

        if category is not None:
            all_products = models.Product.objects.filter(category=category)

    if all_products is None:
        all_products = models.Product.objects.all()

    paginator = Paginator(all_products,4)
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


def product(request,product_id):
    try:
        product = models.Product.objects.get(id=product_id)
    except:
        product = None

    template = get_template('product.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)


def add_to_cart(request,product_id,quantity):
    product = models.Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product,product.price,quantity)
    return redirect('/')


def remove_from_cart(request,product_id):
    product = models.Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('/cart/')


@login_required
def cart(request):
    all_categories = models.Category.objects.all()
    cart = Cart(request)
    template = get_template('cart.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)