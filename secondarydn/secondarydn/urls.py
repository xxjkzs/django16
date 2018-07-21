"""secondarydn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^accounts/',include('registration.backends.hmac.urls')),
    url(r'accounts/profile/$',views.index),
    url(r'dnsmanager/$',views.dnsmanager),
    url(r'delsubdomain/(\w+)/$',views.del_subdomain),
    url(r'delrecord/(\d+)/$',views.del_record),
    url(r'addrecord/(\w+)/$',views.add_record),
]
