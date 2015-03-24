#encoding:utf-8

from django import forms


class FormsDateCurrent(forms.Form):

	date_current = forms.DateTimeField(required=False,
                              		   widget=forms.HiddenInput())

	
	def __init__(self, *args, **kwargs):
		self.date = kwargs.pop('obj')
		super(FormsDateCurrent, self).__init__(*args, **kwargs)

		self.fields['date_current'].initial =  self.date