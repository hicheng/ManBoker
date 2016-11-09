# -*- coding:UTF-8 -*-
from selenium import webdriver
from time import sleep
import Desired_capabilities
import os
import unittest

#未登录账号时, 通过登录界面登录
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class elementA(unittest.TestCase):
    def test_(self):
        desired_caps = Desired_capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(5)
        print u'设备配置成功'
        #点击头像登录
        
        go_login =self.driver.find_element_by_id('com.manboker.headportrait:id/entry_album_set')
        go_login.click()
        sleep(5)
        click_head_portrait = self.driver.find_element_by_id('com.manboker.headportrait:id/set_log_out')
        click_head_portrait.click()

        login = self.driver.find_element_by_name("其他登录方式")
        login.click()
        #输入用户名
        username = self.driver.find_element_by_name("手机号码/邮箱")
        username.send_keys("13215998390")
        #输入密码
        possword = self.driver.find_element_by_id('com.manboker.headportrait:id/login_password')
        possword.send_keys("123456")
 #       driver.press_keycode(4)

        #点击登录按钮
        login_btn = self.driver.find_element_by_id("com.manboker.headportrait:id/login_submit")
        login_btn.click()
        sleep(2)
    def exitApp(cls):
        cls.driver.close_app()
        cls.driver.quit()
        print u'退出程序'


