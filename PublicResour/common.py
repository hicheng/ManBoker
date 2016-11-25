# -*- coding:utf-8 -*-
import os
from selenium.webdriver.support.ui import WebDriverWait

def swipe_left(self):
    print "start swipe left"
    # 获取手机屏幕的宽、高
    width = self.driver.get_window_size()['width']
    height = self.driver.get_window_size()['height']
    self.driver.swipe(width*4/5, height/2, width*1/5, height/2, 1000)

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

