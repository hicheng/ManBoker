# -*- coding:utf-8 -*-
from appium import webdriver
import unittest
from PublicResour import Desired_Capabilities
from time import sleep
'''
测试首页电商
'''
class DianShang(object):

    def SetUp(self):
        desired_caps = Desired_Capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print u"设备配置成功"
        sleep(5)
        homeDshang = self.driver.find_elements_by_class_name("android.view.View")
        homeDshang[1].click()
        sleep(8)
        print self.driver.page_source
        print self.driver.context
        self.driver.switch_to.context("WEBVIEW_com.android.browser")
    def testChinese(self):
        '''
        简体中文电商
        :return:
        '''

DianShang().SetUp()
'''
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DianShang)
    unittest.TextTestRunner(verbosity=2).run(suite)
'''