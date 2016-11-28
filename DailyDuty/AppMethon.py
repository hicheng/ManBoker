# -*- coding:utf-8 -*-
'''
这个脚本暂时未启用
'''
from time import sleep
from selenium import webdriver
import os
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def CreateDir(filepath):
    '''
    判断当前路径是否需要创建文件夹
    :param filepath:
    :return:
    '''
    current_path = sys.path[0]
    if os.path.exists(current_path + filepath):
        pass
    else:
        os.makedirs(current_path + filepath)

def ShootBackgroundMethon(self):
    '''
    1. 做漫画界面和拍背景界面截图
    2. 做漫画到拍背景整个流程
    :param self:
    :return:
    '''
    # 等待收藏图标加载出来后截图
    WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_id("com.manboker.headportrait:id/comic_praise_iv"))
    self.driver.get_screenshot_as_file(sys.path[0] + "/Screenshot/favorite/" + time.strftime('%H-%M-%S', time.localtime()) + '.jpg')

    # 拍背景
    self.driver.find_element_by_name("创作").click()
    self.driver.find_element_by_id("com.manboker.headportrait:id/sign_change_bg_layout").click()
    self.driver.find_element_by_name("拍背景").click()
    WebDriverWait(self.driver, 30).until(
        lambda x: x.find_element_by_id("com.manboker.headportrait:id/change_bg_take_picture"))
    self.driver.get_screenshot_as_file(sys.path[0] + "/Screenshot/background/" + time.strftime('%H-%M-%S', time.localtime()) + '.jpg')
    # 返回
    change_bg_back = self.driver.find_element_by_id("com.manboker.headportrait:id/change_bg_back_iv")
    change_bg_back.click()
    sleep(1)
    set_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback")
    set_goback.click()
    set_goback.click()

def  NormalLogin(self, accountnumber, password):
    '''
    1. 在首页点击右下角头像图标从而判断账号是否已登录
    2. 根据已登录和未登录下的头像id不同来判断
    :param self:
    :param accountnumber:
    :param password:
    :return:
    '''
    try:
    # 判断账号是否登录
        WebDriverWait(self.driver, 5).until(lambda  x: x.find_element_by_id("com.manboker.headportrait:id/entry_album_set")).click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_log_out").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_other").click()
        # 清除输入框内的内容
        login_user = self.driver.find_element_by_id("com.manboker.headportrait:id/login_user")
        login_user.clear()
        login_user.send_keys(accountnumber)
        login_password = self.driver.find_element_by_id("com.manboker.headportrait:id/login_password")
        login_password.send_keys(password)
        login_submit = self.driver.find_element_by_id("com.manboker.headportrait:id/login_submit")
        login_submit.click()
    except:
        print "您已登录账号"

