#-*-encoding:utf-8 -*-   
# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from django.test import LiveServerTestCase
from django.template.loader import render_to_string
from django.test import TestCase, Client
from UserContacts.models import Person, Phone
from UserContacts.views import *
        
class ViewTest(TestCase):
    def setUp(self):
        self.client_stub = Client()
        self.person = Person(firsst_name='TestFirst',last_namt='TestLast')
        self.person.save()
        self.phone=Phone(person=self.person,number='7778889999')
        self.phone.save()
        
    def test_view_home_route(self):
        response = self.client_stub.get('/usercontacts')
        print(response)
        self.assertEquals(response.status_code, 200)
        
    def test_view_contacts_route(self):
        response = self.client_stub.get('/usercontacts/all')
        self.assertEqual(response.status_code,200,)