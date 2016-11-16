# -*- coding:utf-8 -*-
from selenium import webdriver
from appium import webdriver
import unittest
from time import sleep
import Desired_Capabilities
import os
#import AppException

# Return ads path relative to this file not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class aboutComic(unittest.TestCase):
    def setUp(self):
        desired_caps = Desired_Capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print u'设备配置成功'
        sleep(10)


    def bgShare(self):
        '''
        拍背景和保存分享
        :return:  封装
        '''
        # 进入创作
        enter_click = self.driver.find_element_by_name("创作")
        enter_click.click()
        sleep(3)
        # 拍背景
        select_background = self.driver.find_element_by_id("com.manboker.headportrait:id/sign_change_bg_layout")
        select_background.click()
        sleep(2)
        background = self.driver.find_element_by_name("拍背景")
        background.click()
        sleep(5)
        back_background = self.driver.find_element_by_id("com.manboker.headportrait:id/change_bg_back_iv")
        back_background.click()
        sleep(2)
        # 保存分享漫画
        save_share = self.driver.find_element_by_name("保存/分享")
        save_share.click()
        sleep(5)
        # 返回下一张漫画拍背景
        save_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/comic_save_goback")
        save_goback.click()
        sleep(1)
        set_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback")
        set_goback.click()
        sleep(1)


    def test_backGroundAndSaveShare(self):
        '''
        先拍背景再保存分享
        :return:
        '''
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[0].click()
        sleep(8)
        aboutComic().bgShare()
        # 向左滑动显示第一张更新的漫画
        self.driver.swipe(300, 900, 1000, 900, 3000)
        aboutComic().bgShare()
        # 从做漫画返回到首页
        back_makecomic = self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_top_view_to_entry_iv")
        back_makecomic.click()
        sleep(5)

    def tear_Down(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(aboutComic)
    unittest.TextTestRunner(verbosity=2).run(suite)
