# -*- coding:UTF-8 -*-
from selenium import webdriver
import time
import unittest

project_path = "C:\Pycharm\EyebrowsAlgorithm"
class startDevices(unittest.TestCase):
    def start(self):
        desired_caps = {}
        desired_caps['deviceName'] = '0123456789ABCDEF'  # adb devices查到的设备名
        desired_caps['platformName'] = 'Android'    #测试平台名称
        desired_caps['platformVersion'] = '4.4.2'     # 待测手机的系统版本号
        desired_caps['appPackage'] = 'com.manboker.headportrait'  # 被测App的包名
        desired_caps['appActivity'] = '.activities.EntryActivity'    # 打开界面的Activity， 获得appActivity详情见http://www.cnblogs.com/kllay/p/5506480.html
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)
        enter = driver.find_element_by_id('com.manboker.headportrait:id/home_top_inner')
        enter.click()