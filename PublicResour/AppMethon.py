# -*- coding:utf-8 -*-
'''

'''
from time import sleep
import os
import sys
import time
import shutil
from selenium.webdriver.support.ui import WebDriverWait


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def CreateDir(filepath):
    '''
    判断当前路径是否存在文件夹
    如果存在就删除后创建文件夹
    :param filepath:
    :return:
    '''
    current_path = sys.path[0]

    if os.path.exists(current_path + filepath):
        try:
            print "2"
            shutil.rmtree(current_path + filepath)      #删除文件夹， 文件夹中包含子文件
            sleep(2)
            os.makedirs(current_path + filepath)
        except:
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
    sleep(1)
    self.driver.find_element_by_name("创作").click()
    self.driver.find_element_by_id("com.manboker.headportrait:id/sign_change_bg_layout").click()
    self.driver.find_element_by_name("拍背景").click()
    WebDriverWait(self.driver, 30).until(
        lambda x: x.find_element_by_id("com.manboker.headportrait:id/change_bg_take_picture"))
    self.driver.get_screenshot_as_file(sys.path[0] + "/Screenshot/background/" + time.strftime('%H-%M-%S', time.localtime()) + '.jpg')
    sleep(1)
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
        WebDriverWait(self.driver, 5).until(lambda  x: x.find_element_by_id("com.manboker.headportrait:id/entry_album_set")).click()  #头像icon进行判断
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

def TakePicturesTutorial(self):
    '''
    首次安装App时的拍照教程
    :param self:
    :return:
    '''
    try:
        WebDriverWait(self.driver, 5).until(
            lambda x: x.find_element_by_id("com.manboker.headportrait:id/take_picture")).click() #判断是否进入拍照流程
        #默认做男性头像选择中年男子
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_id("com.manboker.headportrait:id/iv_gender_man")).click()
        WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_id("背景")).click()
        print u'拍照教程已完成'
    except:
        pass

CreateDir('\Test')