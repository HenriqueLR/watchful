#encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class ControllEmployee(models.Model):
	
	'''
	This simple class, onetoonefield for admin, control 
	auth users and check point workers.
	'''

	id_controll_employee = models.AutoField(primary_key=True, verbose_name=u'Id', db_column='id_controll_employee')
	employee = models.OneToOneField(User, db_column='employee', related_name='employee_user', verbose_name='Colaborador')
	date_entry = models.DateTimeField(verbose_name='Data Entrada', db_column='date_entry', null=True)
	date_out = models.DateTimeField(verbose_name='Data Saida', db_column='date_out', null=True)
	date_created = models.DateTimeField(verbose_name='Data Criação', db_column='date_created', auto_now_add=True)
	month = models.IntegerField(verbose_name='Mês', db_column='month', null=True, default=timezone.now().month)
	year = models.IntegerField(verbose_name='Ano', db_column='year', null=True, default=timezone.now().year)
	day =  models.IntegerField(verbose_name='Dia', db_column='day', null=True, default=timezone.now().day)
	description = models.CharField(verbose_name='Descrição', db_column='description', null=True, 
				       default='Controle de ponto.',max_length=50)

	def __unicode__(self):
		return u'%s' % self.id_controll_employee

	class Meta:
		verbose_name=u'Controle de Colaboradores'
		verbose_name_plural=u'Controle de Colaboradores'
		ordering=['id_controll_employee']
		db_table='controll_employee'	
