# -*- coding:utf-8 -*-
from selenium import webdriver
from appium import webdriver
import unittest
from time import sleep
import Desired_Capabilities
import os
import common

'''
查找h5元素时尝试按住botton时用automator获取元素
'''
#Return ads path relative to this file not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class dailyScore(unittest.TestCase):

    def setUp(self):
        desired_caps = Desired_Capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps )
        print u'设备配置成功'
        sleep(10)

    def testScore(self):

        #进入每日评分
        self.driver.find_element_by_id("com.manboker.headportrait:id/entity_score").click()
        sleep(3)
        self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"魔漫评审员\"]/android.view.View[9]/android.widget.Image[1]").click()
        sleep(5)

        #检查是否开了评分标准
        try:
            self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"魔漫评审员\"]/android.view.View[9]/android.widget.Image[1]").click()
        except:
            pass

        #检查评分标准的图片是否会显示
        self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"评分标准\"]").click()
        self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"魔漫评审员\"]/android.view.View[9]/android.widget.Image[1]").click()

        for i in range(1,4):
            self.driver.find_element_by_xpath("//android.widget.Image[@content-desc=\"100\"]").click()
            sleep(2)

        self.driver.tap([(93, 1685), (1122, 1690)], 500)
        sleep(3)
        self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"5魔豆的奖励请去魔豆商城中使用知道了\"]").click()
        sleep(2)

        #查看昨日的评审结果
        self.driver.tap([(984, 720), (1082, 720)], 500)
        sleep(3)

        #返回
        web_close = self.driver.find_element_by_id("com.manboker.headportrait:id/web_close_btn")
        web_close.click()
        self.driver.find_element_by_name("稍后回来").click()
        print u'-----每日评分检查完毕-----'
        sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(dailyScore)
    unittest.TextTestRunner(verbosity=2).run(suite)