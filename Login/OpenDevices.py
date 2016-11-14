# coding:utf-8
import os
import time
#import HTMLTestRunner
import unittest
from selenium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class elementA(unittest.TestCase):
    def test_(self):
        desired_caps = {}
        desired_caps['deviceName'] = 'QLXBBBB632413840'  # adb devices查到的设备名
        desired_caps['platformName'] = 'Android'    #测试平台名称
        desired_caps['platformVersion'] = '5.1'     # 待测手机的系统版本号
        desired_caps['appPackage'] = 'com.manboker.headportrait'  # 被测App的包名
        desired_caps['appActivity'] = '.activities.SplashActivity'    # 打开界面的Activity， 获得appActivity详情见http://www.cnblogs.com/kllay/p/5506480.html
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)
#        el = driver.find_element_by_id('com.manboker.headportrait:id/set_Rating')
#        self.assertIsNotNone(el)
#        el.click()
        driver.find_element_by_class_name('android.view.View').click()
        #进入做漫画界面
        time.sleep(2)
        driver.find_element_by_id('com.manboker.headportrait:id/comics_main_top_view_to_camera_iv').click()
        # 左上角相机图标
        time.sleep(1)
        driver.find_element_by_id('com.manboker.headportrait:id/set_phoneImage').click()
        #选择手机相册
        time.sleep(1)
        driver.find_element_by_id('com.manboker.headportrait:id/album_item_content').click()
        #选择排序为第一个相册文件夹
        time.sleep(1)
        driver.find_element_by_id('com.manboker.headportrait:id/child_image').click()
        #选择第一张照片
        time.sleep(1)
        driver.find_element_by_id('com.manboker.headportrait:id/iv_gender_man').click()
        #选择性别界面
        time.sleep(1)
        driver.find_element_by_id('com.manboker.headportrait:id/adjust_age_mature_iv').click()
        #选择年龄并拍照
        time.sleep(10)
        driver.find_element_by_id('com.manboker.headportrait:id/comics_main_top_view_to_share_iv').click()
        #保存分享
        time.sleep(2)

        def SelectElements():       #界面查找元素
            el = driver.find_elements_by_id('com.manboker.headportrait:id/child_image')

            for i in range(0,22):
                el[i].click()
                print i
 #       SelectElements()

        def SaveCycle():
            driver.find_element_by_id('com.manboker.headportrait:id/comic_save_goback').click()
            #左上角返回
            time.sleep(2)
            driver.find_element_by_id('com.manboker.headportrait:id/comics_main_top_view_to_camera_iv').click()
            # 右上角拍照
            time.sleep(1)
            driver.find_element_by_id('com.manboker.headportrait:id/set_phoneImage').click()
            # 选择手机相册
            time.sleep(1)
            driver.find_elements_by_id('com.manboker.headportrait:id/album_item_content')
            time.sleep(2)
            driver.find_element_by_id('com.manboker.headportrait:id/child_image').click()
            # 选择第一张照片
            time.sleep(1)
        SaveCycle()
        SelectElements()
 #       time.sleep(10)




