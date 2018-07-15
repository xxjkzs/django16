from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from allauth.account.decorators import verified_email_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from cart.cart import Cart
from paypal.standard.forms import PayPalPaymentsForm
import datetime
from mysite import models,forms

# Create your views here.
def index(request,cat_id=0):
    all_categories = models.Category.objects.all()
    cart = Cart(request)
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


# @verified_email_required
def order(request):
    all_categories = models.Category.objects.all()
    cart = Cart(request)
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        new_order = models.Order(user=user)
    
        form = forms.OrderForm(request.POST,instance=new_order)
        if form.is_valid():
            order = form.save()
            email_messages = 'Here is your new order:\n'
            for item in cart:
                models.OrderItem.objects.create(order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity)
                email_messages += '\n'+'{},{},{}'.format(item.product,
                    item.product.price,
                    item.quantity)
                email_messages += '\n Grand total:{}'.format(cart.summary())
                cart.clear()
                messages.add_message(request,messages.INFO,"Received your order, processing.")  
                send_mail('Thanks for your support.',
                    email_messages,
                    'Mini Online Shop',
                    [request.user.email],)  
                send_mail('Your have a new order',
                    email_messages,
                    'Mini Online Shop',
                    ['xxjkzs@foxmail.com'],)
                return redirect('/myorders/')
    else:
        form = forms.OrderForm()

    template = get_template('order.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)  


@login_required
def my_orders(request):
    all_categories = models.Category.objects.all()
    orders = models.Order.objects.filter(user=request.user)

    template = get_template('myorders.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)


@csrf_exempt
def payment_done(request):
    template = get_template('payment_done.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html) 


@csrf_exempt
def payment_cancelled(request):
    template = get_template('payment_cancelled.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html) 


@login_required
def payment(request,order_id):
    all_categories = models.Category.objects.all()
    try:
        order = models.Order.objects.get(id=order_id)
    except:
        messages.add_message(request,messages.WARNING,"Wrong order ID , fail to process.")
        return redirect('/myorders/')
    all_order_items = models.OrderItem.objects.filter(order=order)
    items = list()
    total = 0
    for order_item in all_order_items:
        t = dict()
        t['name'] = order_item.product.name
        t['price'] = order_item.product.price
        t['quantity'] = order_item.quantity
        t['subtotal'] = order_item.price * order_item.quantity
        total += order_item.product.price
        items.append(t)

        host = request.get_host()
        paypal_dict = {
            'business' : settings.PAYPAL_RECEIVER_EMAIL,
            'amount' : total,
            'item_name' : 'item id : {} '.format(order_id),
            'invoice' : 'invoice-{}'.format(order_id),
            'currency_code' : 'CNY',
            'notify_url' : 'http://{}{}'.format(host,reverse('paypal-ipn')),
            'return_url' : 'http://{}'.format(host),
            'cancel_return' : 'http://{}/cancelled'.format(host),
        }

    paypal_form = PayPalPaymentsForm(initial=paypal_dict)  
    template = get_template('payment.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html) 
