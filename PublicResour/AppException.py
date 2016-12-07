# -*- coding:utf-8 -*-
from time import sleep


'''
用于封装执行过程中偶然出现的异常
'''


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

