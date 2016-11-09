# -*- coding:UTF-8 -*-
from selenium import webdriver
import time
import os
import unittest
#未登录账号时, 通过登录界面登录
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class elementA(unittest.TestCase):
    def test_(self):
        desired_caps = {}
        desired_caps['deviceName'] = '01234567890123456789'  # adb devices查到的设备名
        desired_caps['platformName'] = 'Android'  # 测试平台名称
        desired_caps['platformVersion'] = '4.4.4'  # 待测手机的系统版本号
        desired_caps['appPackage'] = 'com.manboker.headportrait'  # 被测App的包名
        desired_caps[
            'appActivity'] = '.activities.SplashActivity'  # 打开界面的Activity， 获得appActivity详情见http://www.cnblogs.com/kllay/p/5506480.html

        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'  # 后两行解决输入法的问题
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)
        print u'设备配置成功'
        #点击头像登录

        go_login =driver.find_element_by_id('com.manboker.headportrait:id/entry_album_set')
        go_login.click()
        time.sleep(5)
        click_head_portrait = driver.find_element_by_id('com.manboker.headportrait:id/set_log_out')
        click_head_portrait.click()

        login = driver.find_element_by_name("其他登录方式")
        login.click()
        #输入用户名
        username = driver.find_element_by_name("手机号码/邮箱")
        username.send_keys("13215998390")
        #输入密码
        possword = driver.find_element_by_id('com.manboker.headportrait:id/login_password')
        possword.send_keys("123456")
 #       driver.press_keycode(4)

        #点击登录按钮
        login_btn = driver.find_element_by_id("com.manboker.headportrait:id/login_submit")
        login_btn.click()
        time.sleep(2)
    def exitApp(cls):
        cls.driver.close_app()
        cls.driver.quit()
        print u'退出程序'


