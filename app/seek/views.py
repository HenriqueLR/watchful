#encoding: utf-8

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.utils import timezone
from core.models import ControllEmployee
from .forms import FormsDateCurrent



class ControllPoint(View):

	form_class = FormsDateCurrent
	template_name = 'ponto.html'

	@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		date_today = timezone.now()
		context = {}
		context['form'] = self.form_class(user=self.request.user, obj=date_today)
		context['date_current'] = date_today
		context['obj'] = ControllEmployee.objects.filter(employee=self.request.user,year=date_today.year,
								 month=date_today.month,day=date_today.day)
		return render(request, self.template_name, context)

	@method_decorator(login_required)
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, user=self.request.user, obj=timezone.now())
		if form.is_valid():
			if form.save():
				messages.success(request, 'Ponto confirmado!')
			else:
				messages.error(request, 'Não pode mais bater o ponto!')
				
		return redirect('/controle/')