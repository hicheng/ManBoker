# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver


class DefineException(object):

    '''
    用于封装执行过程中偶然出现的异常



    def __init__(self):

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub')
        sleep(3)
    '''

    def exceptionStartHead(self):
        '''
        以防进首页时头像会有可点击的闪光效果
        :return:
        '''
        try:
            avatar = self.driver.find_element_by_id("com.manboker.headportrait:id/guide_change_model_head_anim_view")
            avatar.click()
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