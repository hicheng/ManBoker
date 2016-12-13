# -*- coding:utf-8 -*-
import os, time, HTMLTestRunner
import unittest, BSTestRunner
from time import sleep

from appium import webdriver
from selenium import webdriver

from PublicResour import Desired_Capabilities
from PublicResour import common

#Return ads path relative to this file not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class aboutComic(unittest.TestCase):
    def setUp(self):
        desired_caps = Desired_Capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps )
        print u'设备配置成功'
        sleep(10)

    def testMessageCenter(self):
        '''
        检查社区中消息的功能
        :return:
        '''
        # 进入社区首页
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[3].click()
        sleep(8)

        #查看消息
        comment_notification = self.driver.find_element_by_id("com.manboker.headportrait:id/community_topic_comment_notification")
        comment_notification.click()
        sleep(1)
        md_dynamic = self.driver.find_element_by_name("我")
        md_dynamic.click()
        sleep(2)
        md_system = self.driver.find_element_by_name("系统")
        md_system.click()
        sleep(2)

        #清除所有消息
        history_layout = self.driver.find_element_by_id("com.manboker.headportrait:id/community_notification_history_layout")
        history_layout.click()
        self.driver.find_element_by_name("清空系统消息列表").click()
        self.driver.find_element_by_name("确定").click()

        print u'-----社区系统消息检查完成-----（PASS）'
        #返回首页
        go_home = self.driver.find_element_by_id("com.manboker.headportrait:id/topic_goback")
        go_home.click()
        sleep(2)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(aboutComic)
    #    unittest.TextTestRunner(verbosity=2).run(suite)
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    filename = "C:\Pycharm\ManBoker\\report.html"
    print (filename)
    fp = open(filename, 'w')
    runner = BSTestRunner.BSTestRunner(
        stream=fp,
        title='Test',
        description='aa'
    )
    runner.run(suite)
    fp.close()
