from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import redirect
# from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
# from allauth.account.decorators import verified_email_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from mysite import models

# Create your views here.
def index(request):
    # polls = models.Poll.objects.all()
    all_polls = models.Poll.objects.all().order_by('-created_at')
    paginator = Paginator(all_polls,5)
    p = request.GET.get('p')
    try:
        polls = paginator.page(p)
    except PageNotAnInteger:
        polls = paginator.page(1)
    except EmptyPage:
        polls = paginator.page(paginator,num_pages)

    template = get_template('index.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)


@login_required
# @verified_email_required
def poll(request,pollid):
    try:
        poll = models.Poll.objects.all()
    except:
        poll = None
    if poll is not None:
        pollitems = models.PollItem.objects.filter(poll=poll).order_by('-vote')

    template = get_template('poll.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)


@login_required
# @verified_email_required
def vote(request,pollid,pollitemid):
    try:
        pollitem = models.PollItem.objects.get(id=pollitemid)
    except:
        pollitem = None
    if pollitem is not None:
        pollitem.vote += 1
        pollitem.save()

    target_url = '/poll/' + pollid
    return redirect(target_url)