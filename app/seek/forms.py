#encoding:utf-8

import datetime
from django import forms
from django.utils import timezone
from conf.settings import DATE_HOUR
from django.contrib import messages
from core.models import ControllEmployee



class FormsDateCurrent(forms.Form):

	date_current = forms.DateTimeField(required=False,
                              		   widget=forms.HiddenInput())
	
	def __init__(self, *args, **kwargs):
		self.date = kwargs.pop('obj')
		self.user = kwargs.pop('user')
		super(FormsDateCurrent, self).__init__(*args, **kwargs)

		self.fields['date_current'].initial =  self.date

	def clean(self):
		date_post = self.cleaned_data.get('date_current', None)
		format = datetime.datetime.strptime(str(date_post), DATE_HOUR)
		if self.date.date() != format.date():
			raise forms.ValidationError(u'Houve um problema com as datas!')

	def save(self):
		obj = ControllEmployee.objects.filter(employee=self.user,year=self.date.year,
					       	      month=self.date.month,day=self.date.day)
		if obj.exists():
			if not (obj[0].date_out and obj[0].date_entry):
				obj.update(date_out = self.date)
				return obj
			else:
				return False
		else:
			obj = ControllEmployee(date_entry=self.date, employee=self.user)
			obj.save()
			return obj
