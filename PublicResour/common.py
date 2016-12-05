# -*- coding:utf-8 -*-
import os
from selenium.webdriver.support.ui import WebDriverWait


def swipe_left(self):
    print "start swipe left"
    # 获取手机屏幕的宽、高
    width = self.driver.get_window_size()['width']
    height = self.driver.get_window_size()['height']
    self.driver.swipe(width*5/6, height/2, width*1/6, height/2, 1000)

def customize_swipe_left(self, widthx, heighty, widthx1, heighty1):
    print "start swipe left"
    # 获取手机屏幕的宽、高
    self.driver.swipe(widthx, heighty, widthx1, heighty1, 1000)

# 实现从手机屏幕1/4向右滑动到3/4
def swipe_right(self):
    print "start swipe right"
    # 获取手机屏幕的宽、高
    width = self.driver.get_window_size()['width']
    height = self.driver.get_window_size()['height']
    self.driver.swipe(width * 1 / 5, height / 2, width * 4 / 5, height / 2, 1000)

def wait_appear_by_id(self, id, timeout):
    print "wait element appear"
    WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_id(id), "E\元素未出现")


def wait_appear_by_class_name(self, class_name, timeout):
    print "wait element appear"
    WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_class_name(class_name), "E\元素未出现")


def wait_appear_by_xpath(self, xpath, timeout):
    print "wait element appear"
    WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_xpath(xpath), "E\元素未出现")


def wait_appear_by_name(self, name, timeout):
    print "wait element appear"
    WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_name(name), "E\元素未出现")


#等待某个元素消失
def wait_disappear_by_id(self, id, timeout):
    print "wait element appear"
    WebDriverWait(self.driver, timeout).until_not(lambda driver: driver.find_element_by_id(id), "E\元素未消失")

#退出账号
def Account_out(self):
    self.driver.find_element_by_name("设置").click()
    self.driver.find_element_by_name("退出登录").click()
    self.driver.find_element_by_name("确定").click()
    WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id("android:id/button1"))

#三方登录
def Account_in(self):
    '''
    先判断是否已登录账号
    :param self:
    :return:
    '''
    try:
        # 在登录时进入“我的”界面
        album_set = self.driver.find_element_by_id("com.manboker.headportrait:id/entry_album_set")
        album_set.click()
    except:
        #已有账号登录
        entry_album = self.driver.find_element_by_id("com.manboker.headportrait:id/entry_album_set_icon")
        entry_album.click()
        Account_out(self)
    # 点击头像
    click_head_portrait = self.driver.find_element_by_id('com.manboker.headportrait:id/set_log_out')
    click_head_portrait.click()
    # 点击其它方式登录
    login = self.driver.find_element_by_name("其他登录方式")
    login.click()

