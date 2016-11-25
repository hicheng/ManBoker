# -*- coding:utf-8 -*-
from PublicResour import Desired_Capabilities
from selenium import webdriver
from appium import webdriver
import os
import sys
import time
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from PublicResour import common



class TestYangRan(unittest.TestCase):



    def setUp(self):
        desired_caps = Desired_Capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps )
        self.driver.implicitly_wait(30)
        print u'设备配置成功'

    def test_testcomic(self):
        #关闭导航界面
        page_close = self.driver.find_element_by_id("com.manboker.headportrait:id/news_page_close")
        page_close.click()

        #进入做漫画界面
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[0].click()

        # 等待收藏图标加载出来后截图
        WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_id("com.manboker.headportrait:id/comic_praise_iv"))
        self.driver.get_screenshot_as_file("C:\Pycharm\ManBoker\YrTest\Screenshot")

        # 拍背景
        self.driver.find_element_by_name("创作").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_change_bg_layout").click()
        self.driver.find_element_by_name("拍背景").click()
        WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_id("com.manboker.headportrait:id/change_bg_take_picture"))
        self.driver.get_screenshot_as_file("C:\Pycharm\ManBoker\YrTest\Screenshot")

        # 返回
        change_bg_back = self.driver.find_element_by_id("com.manboker.headportrait:id/change_bg_back_iv")
        change_bg_back.click()
        sleep(1)
        set_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback")
        set_goback.click()
        set_goback.click()

        #向左滑动
        for i in range(1, 100):
            common.swipe_left(self)
#            self.driver.swipe(1050, 900, 300, 900, 1000)
            try:
                self.driver.find_element_by_name("点击漫画左下角的收藏按钮即可添加到我的收藏频道").click()
                print u"----图已测完， 到了我的收藏界面-----"
            except:
                print i

            # 等待收藏图标加载出来后截图
            print time
            WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_id("com.manboker.headportrait:id/comic_praise_iv"))
            self.driver.get_screenshot_as_file("C:\Pycharm\ManBoker\YrTest\Screenshot")
            print time-time
            # 拍背景
            self.driver.find_element_by_name("创作").click()
            self.driver.find_element_by_id("com.manboker.headportrait:id/sign_change_bg_layout").click()
            self.driver.find_element_by_name("拍背景").click()
            WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_id("com.manboker.headportrait:id/change_bg_take_picture"))
            self.driver.get_screenshot_as_file("C:\Pycharm\ManBoker\YrTest\Screenshot")

            # 返回
            change_bg_back = self.driver.find_element_by_id("com.manboker.headportrait:id/change_bg_back_iv")
            change_bg_back.click()

            set_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback")
            set_goback.click()
            set_goback.click()


if __name__ == "__main__":
    current_path = sys.path[0]
    Current_time = time.strftime('%y-%m-%d %X', time.localtime())
    Current_day = time.strftime('%y-%m-%d', time.localtime())
    if os.path.exists(current_path + '/error/' + Current_day + '/'):
        pass
    else:
        os.makedirs(current_path + '/error/' + Current_day)
    ErrorPicDir = 'error/' + Current_day + '/'

    suite = unittest.TestLoader().loadTestsFromTestCase(TestYangRan)
    unittest.TextTestRunner(verbosity=2).run(suite)






