#encoding: utf-8

from django.test import TestCase
from django.contrib.auth.models import User



class TestViewsRoutines(TestCase):

    '''
    Simple class for testing routines views.
    '''

    def setUp(self):
        self.user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
    
    def tearDown(self): 
        del self.user

    def test_redirect_login_point(self):
        response = self.client.get('/controle/')
        self.assertRedirects(response, '/?next=/controle/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/controle/ponto/')
        self.assertRedirects(response, '/?next=/controle/ponto/')
        self.assertEqual(response.status_code, 302)

    def test_redirect_login_admin(self):
        response = self.client.get('/acesso/')
        self.assertRedirects(response, '/acesso/login/?next=/acesso/')
        self.assertEqual(response.status_code, 302)

    def test_controll_point(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/controle/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_admin_acesso(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/acesso/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_add_points(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/controle/ponto/', follow=True)
        self.assertContains(
            response,
            u'Ponto de entrada confirmado!'
        )

        response = self.client.get('/controle/ponto/', follow=True)
        self.assertContains(
            response,
            u'Ponto de saida confirmado!'
        )
        
        response = self.client.get('/controle/ponto/', follow=True)
        self.assertContains(
            response,
            u'Não pode mais bater o ponto!'
        )

    def test_view_logout(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/logout/', follow=True)
        self.assertEqual(response.status_code, 200)