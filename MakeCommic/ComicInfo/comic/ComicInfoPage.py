# -*- coding:utf-8 -*-
# 登录状态下检查漫画信息页的功能

from selenium import webdriver
from appium import webdriver
#import unittest
from time import sleep
import os
import Desired_capabilities
# Return ads path relative to this file not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class ComicInfoPage:
    def start(self):
        desired_caps = Desired_capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(5)
        print u'设备配置成功'


 #   def close(self):
 #       self.driver.quit()

        print u'进入首页了----'
        make_commic = self.driver.find_elements_by_class_name("android.view.View")
        make_commic[0].click()
        sleep(5)
        commit_btn = self.driver.find_element_by_id("com.manboker.headportrait:id/commit_btn")
        commit_btn.click()
        sleep(2)
        self.driver.get_screenshot_as_file('C:\Pycharm\Manboker\ComicInfoPage\screenshot'+ '.jpg')
        print u'开始评分'
        star_rating = self.driver.find_elements_by_class_name("android.widget.ImageView")
        star_rating[4].click()
        sleep(1.5)
        # 打标签
        tag = self.driver.find_element_by_name("加标签")
        tag.click()

        print u'添加后删除标签'
        add_tag = self.driver.find_element_by_id("com.manboker.headportrait:id/add_tag_et")
        add_tag.click()
        add_tag.send_keys("addtag")
        self.driver.find_element_by_name("添加").click()
        sleep(1)
        delete_tag = self.driver.find_element_by_name("addtag")
        delete_tag.click()
        sleep(1)
        confirm_delete_tag = self.driver.find_element_by_id("android:id/button1")
        confirm_delete_tag.click()
        sleep(1)
        self.driver.find_element_by_id("com.manboker.headportrait:id/add_tag_btn_back").click()
        sleep(2)
        print u"添加感受"
        sleep(5)
        add_feeling = self.driver.find_element_by_id("com.manboker.headportrait:id/add_feeling_et")
        add_feeling.click()
        add_feeling.send_keys("testfeeling")
        self.driver.find_element_by_id("com.manboker.headportrait:id/comic_add_feeling_btn").click()
        sleep(5)

        favorite = self.driver.find_element_by_id("com.manboker.headportrait:id/comit_praise_btn")
        favorite.click()
        sleep(2)
        title_hot = self.driver.find_element_by_id("com.manboker.headportrait:id/comic_info_comit_title_hot_btn")
        title_hot.click()
        sleep(1)
        #向下滑动刷新屏幕

        print u'下来刷新感受'
        self.driver.swipe(1137, 450, 1137, 649, 1000)
        sleep(1)

        print u'检查完成---------'

 #       self.driver.close()

ComicInfoPage().start()

