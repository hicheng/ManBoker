# -*- coding:utf-8 -*-
from selenium import webdriver
from appium import webdriver
from time import sleep
import unittest
from DailyDuty import Desired_Capabilities
'''
运用于测试第三方是否能登录
1.  连上VPN
2.  退出账号
启动cmd 输入appium --session-override
'''

class SocialLogin(unittest.TestCase):

    def setUp(self):

        desired_caps = Desired_Capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

        print u'设备配置成功'

    def FastLogin(self):

        '''
        无法获取动态的手机验证码
        :return:
        '''

    def testWeiBo(self):

        #进入“我的”界面
        album_set = self.driver.find_element_by_id("com.manboker.headportrait:id/entry_album_set")
        album_set.click()
        #点击头像
        click_head_portrait = self.driver.find_element_by_id('com.manboker.headportrait:id/set_log_out')
        click_head_portrait.click()
        #点击其它方式登录
        login = self.driver.find_element_by_name("其他登录方式")
        login.click()
        # 点击微博
        tvWeibo = self.driver.find_element_by_id("com.manboker.headportrait:id/tvWeibo")
        tvWeibo.click()
        sleep(10)
        '''
        print self.driver.contexts
        self.driver.switch_to.context("WEBVIEW_com.android.browser")

        '''
        #输入手机号和密码
        email_phonenumber = self.driver.find_element_by_name("//android.view.View[@content-desc=\"登录 - 新浪微博\"]")
        email_phonenumber.click()
        email_phonenumber.send_keys("13215998390")
        password = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"登录 - 新浪微博\"]/android.widget.EditText[2]")
        password.click()
        password.send_keys("mima123")
        self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"登录 - 新浪微博\"]").click()


