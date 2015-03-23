#encoding: utf-8

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth.models import User



class TestLoginAdmin(LiveServerTestCase):

    '''
    Simple functional test use case interface admin.
    '''

    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(TestLoginAdmin, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestLoginAdmin, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/acesso/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('root')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('root')
        self.selenium.find_element_by_xpath('//input[@value="Acessar"]').click()



class TestLoginPoint(LiveServerTestCase):

    '''
    Simple functional test use case interface watchful.
    '''

    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(TestLoginPoint, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestLoginPoint, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('root')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('root')
        self.selenium.find_element_by_xpath('//input[@value="Entrar"]').click()