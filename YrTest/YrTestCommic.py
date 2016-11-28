# -*- coding:utf-8 -*-
from PublicResour import Desired_Capabilities
from selenium import webdriver
from appium import webdriver
import os
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class TestYangRan(unittest.TestCase):
    def setUp(self):
        desired_caps = Desired_Capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        print u'设备配置成功'
        time.sleep(5)
    def test_testcomic(self):
        # 在本地设置存放截图的文档
        current_path = sys.path[0]
        if os.path.exists(current_path + '/Screenshot/favorite/'):
            pass
        else:
            os.makedirs(current_path + '/Screenshot/favorite/')

        if os.path.exists(current_path + '/Screenshot/background/'):
            pass
        else:
            os.makedirs(current_path + '/Screenshot/background/')

        #关闭导航页
        page_close = self.driver.find_element_by_id("com.manboker.headportrait:id/news_page_close")
        page_close.click()

        #判断是否已登录
        try:
            WebDriverWait(self.driver, 3).until(
                lambda x: x.find_element_by_id("com.manboker.headportrait:id/entry_album_set")).click()
            self.driver.find_element_by_id("com.manboker.headportrait:id/set_log_out").click()
            self.driver.find_element_by_id("com.manboker.headportrait:id/set_other").click()

            login_user = self.driver.find_element_by_id("com.manboker.headportrait:id/login_user")
            login_user.clear()
            login_user.send_keys("18500307774")
            login_password = self.driver.find_element_by_id("com.manboker.headportrait:id/login_password")
            login_password.send_keys("yr.0411")
            login_submit = self.driver.find_element_by_id("com.manboker.headportrait:id/login_submit")
            login_submit.click()
        except:
            print "您已登录账号"

        #从我的界面进入首页
        try:
            home_page = WebDriverWait(self.driver, 2).until(lambda x: x.find_element_by_id("com.manboker.headportrait:id/set_set_goback"))
            home_page.click()
        except:
            pass

        #进入做漫画界面
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[0].click()

        #等我的收藏图标加载出来后截图
        WebDriverWait(self.driver, 5).until(
            lambda x: x.find_element_by_id("com.manboker.headportrait:id/comic_praise_iv"))
        self.driver.get_screenshot_as_file(current_path + "/Screenshot/favorite/" + time.strftime('%H-%M-%S', time.localtime()) + '.jpg')
        time.sleep(5)

        #拍背景流程
        self.driver.find_element_by_name("创作").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_change_bg_layout").click()
        self.driver.find_element_by_name("拍背景").click()
        WebDriverWait(self.driver, 5).until(
            lambda x: x.find_element_by_id("com.manboker.headportrait:id/change_bg_take_picture"))
        self.driver.get_screenshot_as_file(current_path + "/Screenshot/background/" + time.strftime('%H-%M-%S', time.localtime()) + '.jpg')

        # 返回
        change_bg_back = self.driver.find_element_by_id("com.manboker.headportrait:id/change_bg_back_iv")
        change_bg_back.click()
        time.sleep(1)
        set_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback")
        set_goback.click()
        set_goback.click()

        #循环滑动下一张
        for i in range(1, 100):
            width = self.driver.get_window_size()['width']
            height = self.driver.get_window_size()['height']
            self.driver.swipe(width * 4 / 5, height / 2, width * 1 / 5, height / 2, 1000)

            #滑动直到出现“点击漫画左下角的收藏按钮即可添加到我的收藏频道”
            try:
                WebDriverWait(self.driver, 5).until(
                    lambda x: x.find_element_by_name("点击漫画左下角的收藏按钮即可添加到我的收藏频道"))
                print u"----图已测完， 到了我的收藏界面-----"
                self.driver.quit()
            except:
                print i

            # 等我的收藏图标加载出来后截图
            WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_id("com.manboker.headportrait:id/comic_praise_iv"))
            self.driver.get_screenshot_as_file(current_path + "/Screenshot/favorite/"+ time.strftime('%H-%M-%S', time.localtime()) + '.jpg')
            print current_path + "/Screenshot/favorite/"+ time.strftime('%H:%M:%S', time.localtime()) + '.jpg'

            #拍背景流程
            self.driver.find_element_by_name("创作").click()
            self.driver.find_element_by_id("com.manboker.headportrait:id/sign_change_bg_layout").click()
            self.driver.find_element_by_name("拍背景").click()
            WebDriverWait(self.driver, 30).until(
                lambda x: x.find_element_by_id("com.manboker.headportrait:id/change_bg_take_picture"))
            self.driver.get_screenshot_as_file(current_path + "/Screenshot/background/"+ time.strftime('%H-%M-%S', time.localtime()) + '.jpg')

            #返回
            change_bg_back = self.driver.find_element_by_id("com.manboker.headportrait:id/change_bg_back_iv")
            change_bg_back.click()
            time.sleep(1)
            set_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback")
            set_goback.click()
            set_goback.click()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestYangRan)
    unittest.TextTestRunner(verbosity=2).run(suite)







