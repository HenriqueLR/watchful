#encoding: utf-8

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.utils import timezone
from core.models import ControllEmployee
from .forms import FormsDateCurrent
from conf.settings import DATE_HOUR
import datetime



class ControllPoint(View):

	form_class = FormsDateCurrent
	template_name = 'ponto.html'

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		date_today = timezone.now()
		context = {}
		context['form'] = self.form_class(obj=date_today)
		context['date_current'] = date_today
		context['obj'] = ControllEmployee.objects.filter(employee=self.request.user,year=date_today.year,
									 					 month=date_today.month,day=date_today.day)
		return render(request, self.template_name, context)

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		date_today = datetime.datetime.strptime(request.POST.get("date_current", ""), DATE_HOUR)
		obj = ControllEmployee.objects.filter(employee=request.user,year=date_today.year,
					      				  	  month=date_today.month,day=date_today.day)

		if obj.exists():
			if not (obj[0].date_out and obj[0].date_entry):
				obj.update(date_out = date_today)
				messages.success(request, 'Ponto de saida confirmado!')
			else:
				messages.error(request, 'Não pode mais bater o ponto!')	
		else:
			obj = ControllEmployee(date_entry=date_today, employee=request.user)
			obj.save()
			messages.success(request, 'Ponto de entrada confirmado!')

		return redirect('/controle/')