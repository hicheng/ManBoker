# -*- coding:utf-8 -*-
from selenium import webdriver
from appium import webdriver
from time import sleep
import unittest
from PublicResour import Desired_Capabilities
from selenium.webdriver.support.ui import WebDriverWait
from PublicResour import common
'''
运用于测试第三方是否能登录
1.  连上VPN
2.  退出账号
启动cmd 输入appium --session-override
'''

class SocialLogin(unittest.TestCase):

    def setUp(self):

        desired_caps = Desired_Capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

        print u'设备配置成功'

        common.Account_in(self)

    def FastLogin(self):

        '''
        无法获取动态的手机验证码
        :return:
        '''

    def testWeiBo(self):

        # 点击微博
        tvWeibo = self.driver.find_element_by_id("com.manboker.headportrait:id/tvWeibo")
        tvWeibo.click()

        '''
        #切换混合型View
        print self.driver.contexts
        self.driver.switch_to.context("WEBVIEW_com.android.browser")

        '''
        #输入手机号和密码
        email_phonenumber = WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_xpath("//android.view.View[@content-desc=\"登录 - 新浪微博\"]/android.widget.EditText[1]"))
        email_phonenumber.send_keys("13215998390")
        password = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"登录 - 新浪微博\"]/android.widget.EditText[2]")
        password.send_keys("mima123")
        self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"登录 - 新浪微博\"]").click()
        print "s"
        #检查是否有确认登录按钮
        try:
            self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"确认 Link\"]").click()
        except:
            pass
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("com.manboker.headportrait:id/imageView_head"))
        print u'微博成功登录'

        #退出账号
        common.Account_out(self)
        sleep(4)
    def testQq(self):

        #点击QQ
        tvQq = self.driver.find_element_by_id("com.manboker.headportrait:id/tvQq")
        tvQq.click()
        sleep(10)

        #输入手机号和密码
        email_phonenumber = WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_xpath("//android.view.View[@content-desc=\"QQ登录\"]/android.view.View[2]/android.widget.EditText[1]"))
        email_phonenumber.send_keys("3434633002")
        password = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"QQ登录\"]/android.view.View[3]/android.widget.EditText[1]")
        password.send_keys("mima123")
        self.driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登 录\"]").click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("com.manboker.headportrait:id/imageView_head"))
        print u'QQ成功登录'
        # 退出账号
        common.Account_out(self)
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SocialLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)