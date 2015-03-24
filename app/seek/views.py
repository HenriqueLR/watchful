#encoding: utf-8

from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from core.models import ControllEmployee
from django.utils import timezone



@login_required
def add_point(request):
	date_today = timezone.now()
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



class ControllView(TemplateView):

	template_name = "ponto.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ControllView, self).dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		self.date_today = timezone.now()
		context = super(ControllView, self).get_context_data(**kwargs)
		context['date_current'] = self.date_today
		context['obj'] = ControllEmployee.objects.filter(employee=self.request.user,year=self.date_today.year,
								 month=self.date_today.month,day=self.date_today.day)
		return context
