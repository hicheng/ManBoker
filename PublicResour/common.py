# -*- coding:utf-8 -*-
import os
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

'''
切换webview
webview = self.driver.contexts[1]
        print webview
        self.driver.switch_to.context(webview)
'''
def swipe_left(self):
    # 获取手机屏幕的宽、高
    width = self.driver.get_window_size()['width']
    height = self.driver.get_window_size()['height']
    self.driver.swipe(width*6/7, height/2, width*1/7, height/2, 1000)

def swipe_right(self):
    # 获取手机屏幕的宽、高
    width = self.driver.get_window_size()['width']
    height = self.driver.get_window_size()['height']
    self.driver.swipe(width * 1 / 5, height / 2, width * 4 / 5, height / 2, 1000)

def wait_appear_by_name(self, name, timeout):
    print "wait element appear"
    WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element_by_name(name), "未出现")

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

def exceptionStartHead(self):
    '''
    点击全屏幕
    以防进首页时头像会有可点击的闪光效果等
    :return:
    '''
    try:
        self.driver.find_element_by_class_name("android.widget.FrameLayout").click()
        sleep(2)
    except:
        pass

def exceptionActivityView(self):
    '''
    检查活动专区页面的活动详情， if活动详情打开就关闭
    :return:
    '''
    try:
        check_view = self.driver.find_element_by_name("查看活动详情")
        check_view.click()
        sleep(2)
        check_putaway = self.driver.find_element_by_name("收起")
        check_putaway.click()
        sleep(2)
    except:
        check_putaway = self.driver.find_element_by_name("收起")
        check_putaway.click()
        sleep(2)