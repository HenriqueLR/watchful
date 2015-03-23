#encoding: utf-8

from django.test import TestCase
from core.models import ControllEmployee
from django.contrib.auth.models import User
from django.utils import timezone



class TestControllEmployeeModel(TestCase):

    '''
    Simple functional test for the model ControllEmployee.
    '''

    def setUp(self):
        self.user = User.objects.create_user(username='admin', email='admin@admin.com', 
                                             password='admin')
        self.point = ControllEmployee.objects.get_or_create(employee=self.user)
    
    def tearDown(self): 
        del self.user
        del self.point

    def test_defaults_point(self):
        points = ControllEmployee()
        self.assertEqual(points.id_controll_employee, None)
        self.assertEqual(points.date_entry, None)     
        self.assertEqual(points.year, timezone.now().year)
        self.assertEqual(points.month, timezone.now().month)
        self.assertEqual(points.date_created, None)
        self.assertEqual(points.day, timezone.now().day)  
        self.assertEqual(points.date_out, None) 

    def test_created_point(self):
        self.assertEqual(ControllEmployee.objects.count(), 1)

    def test_created_user(self):
        self.assertEqual(User.objects.count(), 1)