# -*- coding:utf-8 -*-
import os
import sys
from selenium import webdriver
from time import sleep
from appium import webdriver

'''
滑动轨迹测试 tap、swipe、 flick
'''
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname("C:\Pycharm\ManBoker"), p)
)




def startdevices():
    desired_caps = {}
    desired_caps = {}
    desired_caps['deviceName'] = '01234567890123456789'  # adb devices查到的设备名
    desired_caps['platformName'] = 'Android'  # 测试平台名称
    desired_caps['platformVersion'] = '4.4.4'  # 待测手机的系统版本号
    desired_caps['appPackage'] = 'com.manboker.headportrait'  # 被测App的包名
    desired_caps['appActivity'] = '.activities.SplashActivity'  # 打开界面的Activity， 获得appActivity详情见http://www.cnblogs.com/kllay/p/5506480.html
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboard'] = 'True'  # 后两行解决输入法的问题
    desired_caps['newCommandTimeout'] = 120
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(8)
    enter_makecomic = driver.find_elements_by_class_name("android.view.View")
    enter_makecomic[0].click()
    sleep(8)
    enter_click = driver.find_element_by_name("创作")
    enter_click.click()
    sleep(3)
    driver.find_element_by_id("com.manboker.headportrait:id/create_sign").click()
    sleep(1)
    #尝试tap滑动
    driver.tap([(1089, 646)], 1000)
    sleep(2)
    #尝试swipe滑动
    driver.swipe(53, 118, 1101, 1696, 1000)
    sleep(2)
    #尝试flick滑动
    driver.flick(446, 1042, 775, 1038)
    sleep(2)



'''
tap只是模拟手指点击坐标点
第一次测试结果： 二种滑动方式都是直线
第二次测试结果： flick失败，可能是两个坐标点之间的距离太长（Message: The coordinates provided to an interactions operation are invalid.）
'''
startdevices()