# -*- coding:utf-8 -*-
#import unittest

from appium import webdriver
from appium.common.exceptions import NoSuchContextException
import test
import time

class ContextSwitchingTests(object):
    def setUp(self):
        desired_caps = test.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)
        print u'设备配置成功'


ContextSwitchingTests().setUp()