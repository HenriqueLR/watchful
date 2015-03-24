#encoding: utf-8

from django.contrib import admin
from .models import ControllEmployee



class ControllEmployeeAdmin(admin.ModelAdmin):

	'''
    	listing the fields of model ControllEmployee, in admin application.
    	'''
    
	list_display = ('employee', 'date_entry', 'date_out')


admin.site.register(ControllEmployee, ControllEmployeeAdmin)
