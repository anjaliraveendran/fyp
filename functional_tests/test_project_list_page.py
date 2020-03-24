from selenium import webdriver
from landingpage.models import EmpresDomesticWildHuman
from django.contrib.staticfiles.testing import LiveServerTestCase
from django.urls import reverse
import time

class SeleniumTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver')

    def open(self,url):
        self.browser.get("%s%s" % (self.live_server_url, url))






