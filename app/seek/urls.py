#encoding: utf-8

from django.conf.urls import patterns, include, url
from .views import ControllView


urlpatterns = patterns(
	'seek.views',
	url(r'^$', ControllView.as_view(), name='controll'),
	url(r'^ponto/$', 'add_point', name='add_point'),
)