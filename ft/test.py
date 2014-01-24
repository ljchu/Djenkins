#-*-encoding:utf-8 -*-   
# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from django.test import LiveServerTestCase
from django.template.loader import render_to_string
from django.test import TestCase, Client
from UserContacts.models import Person, Phone
from UserContacts.views import *
# class AdminTest(LiveServerTestCase):
#     #python manage.py dumpdata auth.User --indent=2 > ft/fixtures/admin.json
#     fixtures = ['Djenkins.json']
#     
#     @classmethod
#     def setUpClass(cls):
#         cls.browser = WebDriver()
#         super(AdminTest, cls).setUpClass()
# 
#     @classmethod
#     def tearDownClass(cls):
#         try:
#             cls.browser.quit()
#             super(AdminTest, cls).tearDownClass()
#         except Exception as e:
#             print(e)
#             import os
#             command = 'taskkill /F /IM chrome.exe'
#             os.system(command) 
# 
#     def test_admin_site(self):    
#         # user opens web browser, navigates to admin page
#         self.browser.get(self.live_server_url + '/admin/')
#         body = self.browser.find_element_by_tag_name('body')
#         self.assertIn('Django administration', body.text)
#         # users types in username and passwords and presses enter
#         username_field = self.browser.find_element_by_name('username')
#         username_field.send_keys('Djenkins')
#         password_field = self.browser.find_element_by_name('password')
#         password_field.send_keys('Djenkins')
#         password_field.send_keys(Keys.RETURN)
#         # login credentials are correct, and the user is redirected to the main admin page
#         body = self.browser.find_element_by_tag_name('body')
#         self.assertIn('Site administration', body.text)
#         # user clicks on the Users link
#         user_link = self.browser.find_elements_by_link_text('Users')
#         user_link[0].click()
#         # user verifies that user live@forever.com is present
#         body = self.browser.find_element_by_tag_name('body')
#         self.assertIn('aljchu@163.com', body.text)
#          
#     def test_create_contact_admin(self):
#         self.browser.get(self.live_server_url + '/admin/')
#         username_field = self.browser.find_element_by_name('username')
#         username_field.send_keys('Djenkins')
#         password_field = self.browser.find_element_by_name('password')
#         password_field.send_keys('Djenkins')
#         password_field.send_keys(Keys.RETURN)
#         # user verifies that user_contacts is present
#         body = self.browser.find_element_by_tag_name('body')
#         self.assertIn('Usercontacts', body.text)
#     
#     def test_add_user_admin(self):
#         self.browser.get(self.live_server_url + '/admin/')
#         username_field = self.browser.find_element_by_name('username')
#         username_field.send_keys('Djenkins')
#         password_field = self.browser.find_element_by_name('password')
#         password_field.send_keys('Djenkins')
#         password_field.send_keys(Keys.RETURN)
#         persons_links = self.browser.find_elements_by_link_text('Persons')
#         persons_links[0].click()
#         # user clicks on the Add person link
#         add_person_link = self.browser.find_element_by_link_text('Add person')
#         add_person_link.click()
#         # user fills out the form
#         self.browser.find_element_by_name('first_name').send_keys("Michael")
#         self.browser.find_element_by_name('last_name').send_keys("Herman")
#         self.browser.find_element_by_name('email').send_keys("michael@realpython.com")
#         self.browser.find_element_by_name('address').send_keys("2227 Lexington Ave")
#         self.browser.find_element_by_name('city').send_keys("San Francisco")
#         self.browser.find_element_by_name('state').send_keys("CA")
#         self.browser.find_element_by_name('country').send_keys("United States")
#         # user clicks the save button
#         self.browser.find_element_by_css_selector("input[value='Save']").click()
#         # the Person has been added
#         body = self.browser.find_element_by_tag_name('body')
#         self.assertIn('Herman, Michael', body.text)
#         # user returns to the main admin screen
#         home_link = self.browser.find_element_by_link_text('Home')
#         home_link.click()
#         # user clicks on the Phones link
#         persons_links = self.browser.find_elements_by_link_text('Phones')
#         persons_links[0].click()
#         # user clicks on the Add phone link
#         add_person_link = self.browser.find_element_by_link_text('Add phone')
#         add_person_link.click()
#         # user finds the person in the drop
#         downel = self.browser.find_element_by_name("person")
#         for option in downel.find_elements_by_tag_name('option'):
#             if option.text == 'Herman, Michael':
#                 option.click()
#                 # user adds the phone numbers
#         self.browser.find_element_by_name('number').send_keys("4158888888")
#         # user clicks the save button
#         self.browser.find_element_by_css_selector("input[value='Save']").click()
#         # the Phone has been added
#         body = self.browser.find_element_by_tag_name('body')
#         self.assertIn('4158888888', body.text)
#         # user logs out
#         self.browser.find_element_by_link_text('Log out').click()
#         body = self.browser.find_element_by_tag_name('body')
#         self.assertIn('Thanks for spending some quality time with the Web site today.', body.text)
        
class ViewTest(TestCase):
    def setUp(self):
        self.client_stub = Client()
        
    def test_view_home_route(self):
        response = self.client_stub.get('/usercontacts')
        print(response)
        self.assertEquals(response.status_code, 200)
        
    def test_view_contacts_route(self):
        response = self.client_stub.get('/usercontacts/all')
        self.assertEqual(response.status_code,200,)