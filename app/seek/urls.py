#encoding: utf-8

from django.conf.urls import patterns, include, url
from .views import ControllPoint


urlpatterns = patterns(
	'seek.views',
	url(r'^$', ControllPoint.as_view(), name='controll'),
)