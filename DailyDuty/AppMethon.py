# -*- coding:utf-8 -*-
'''
这个脚本暂时未启用
'''
from time import sleep
from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def ShootBackgroundMethon(self):
    # 等待收藏图标加载出来后截图
    WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_id("com.manboker.headportrait:id/comic_praise_iv"))
    self.driver.get_screenshot_as_file("C:\Pycharm\ManBoker\YrTest\Screenshot")

    # 拍背景
    self.driver.find_element_by_name("创作").click()
    self.driver.find_element_by_id("com.manboker.headportrait:id/sign_change_bg_layout").click()
    self.driver.find_element_by_name("拍背景").click()
    WebDriverWait(self.driver, 30).until(
        lambda x: x.find_element_by_id("com.manboker.headportrait:id/change_bg_take_picture"))
    self.driver.get_screenshot_as_file("C:\Pycharm\ManBoker\YrTest\Screenshot")

    # 返回
    change_bg_back = self.driver.find_element_by_id("com.manboker.headportrait:id/change_bg_back_iv")
    change_bg_back.click()
    sleep(1)
    set_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback")
    set_goback.click()
    set_goback.click()

def  NormalLogin(self, accountnumber, password):
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

class DefineMethon(object):
    '''
    用于封装重复的步骤
    '''

    def startdevices(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub')

    def methonBackGroundAndSaveShare(self):
        '''
                拍背景和保存分享
                :return:  封装
                '''
        # 进入创作
        DefineMethon().startdevices()
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
