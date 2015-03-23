#encoding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^acesso/', include(admin.site.urls)),
    url(r'^$','django.contrib.auth.views.login',{'template_name':'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'login',}, name='logout'),
    url(r'^controle/', include('seek.urls')),
)