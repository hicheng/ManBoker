# -*- coding:utf-8 -*-
from selenium import webdriver
from appium import webdriver
import unittest
from time import sleep
import Desired_Capabilities
from selenium.webdriver.support.ui import WebDriverWait
import os

#Return ads path relative to this file not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class aboutComic(unittest.TestCase):
    def setUp(self):
        desired_caps = Desired_Capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps )
        self.driver.implicitly_wait(10)

        print u'设备配置成功'
        sleep(10)
    def testa(self):
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[2].click()
        sleep(8)
        print self.driver.page_source

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(aboutComic)
    unittest.TextTestRunner(verbosity=2).run(suite)