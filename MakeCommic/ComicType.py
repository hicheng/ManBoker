# -*- coding:utf-8 -*-
from appium import webdriver
import unittest
from PublicResour import Desired_Capabilities
from time import sleep
from PublicResour import common
from selenium.webdriver.support.ui import WebDriverWait
'''
测试漫画分类功能，查看分类的所有图片
1. 测试手机为蓝魔，如果是小屏手机则要改规律
'''

class CreateComic(unittest.TestCase):

    def setUp(self):
        desired_caps = Desired_Capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print u"设备配置成功"
        sleep(10)
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[0].click()
        sleep(8)



    def tearDown(self):
        self.driver.quit()

    def testSelectType(self):
        '''
        1. 设置等待时间手动切换分类
        2. 左滑动进入下一张图片
        :return:
        '''
        self.driver.find_element_by_name("背景").click()  # 进入背景


        #此处修改分类
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name("推荐")).click()


        try:
            #此处修改循环查看图的次数
            for comic in range(1, 101):
                try:
                    common.swipe_left(self)
                    sleep(2)
                    print u'第%d张图' %comic

                except:
                    print u'翻页出现异常请检查'
        except:
            print u"翻页出现异常请检查"


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(CreateComic)
    unittest.TextTestRunner(verbosity=2).run(suite)