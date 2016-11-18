# -*- coding:utf-8 -*-
from selenium import webdriver
from appium import webdriver
import unittest
from time import sleep
import Desired_Capabilities
from selenium.webdriver.support.ui import WebDriverWait
import os

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

    def testSetting(self):

        #进入我的
        head_icon = self.driver.find_element_by_id("com.manboker.headportrait:id/entry_album_set_icon")
        head_icon.click()
        sleep(1)

        #点击进入设置界面
        set_general = self.driver.find_element_by_name("设置")
        set_general.click()
        sleep(1)
        '''
        #管理黑名单
        set_blacklist = self.driver.find_element_by_name("黑名单管理")
        set_blacklist.click()
        sleep(1)
        #如果list下存在黑名单的情况
        try:
            list_head = self.driver.find_element_by_id("com.manboker.headportrait:id/paise_list_head")
            list_head.click()
            sleep(2)
            set_more = self.driver.find_element_by_id("com.manboker.headportrait:id/specific_user_set_more")
            set_more.click()
            self.driver.find_element_by_name("移出黑名单").click()
            sleep(1)
            self.driver.find_element_by_id("com.manboker.headportrait:id/topic_specific_user_goback").click()
            sleep(1)
            self.driver.swipe(1110, 378, 1110, 1000, 1000)
            sleep(1)
            self.driver.find_element_by_id("com.manboker.headportrait:id/topic_paise_list_goback").click()
            sleep(1)
        except:
            self.driver.find_element_by_id("com.manboker.headportrait:id/topic_paise_list_goback").click()
            sleep(1)


        #收货地址管理
        set_receive_adress = self.driver.find_element_by_name("收货地址管理")
        set_receive_adress.click()
        sleep(5)
        #添加两个收货地址

        for n in range(1,3):
            self.driver.find_element_by_id("com.manboker.headportrait:id/new_address").click()
            sleep(2)
            #选择省市区,默认北京市东城区
            self.driver.find_element_by_name("省、市、区").click()
            sleep(2)
            self.driver.find_element_by_name("确定").click()
            #填写详细地址
            address_detail = self.driver.find_element_by_name("详细地址")
            address_detail.click()
            address_detail.send_keys("Testaddress")
            sleep(1)
            #填写联系人
            consignee_name = self.driver.find_element_by_name("收货人姓名")
            consignee_name.click()
            consignee_name.send_keys("Testname")
            #填写手机号码（暂时未确认手机号码的区号）
            consignee_phonenumber = self.driver.find_element_by_name("手机号码")
            consignee_phonenumber.click()
            consignee_phonenumber.send_keys("13000000000")
            self.driver.find_element_by_name("保存").click()
            sleep(2)
            '''
        #更换默认地址
        '''
        因为更改默认收货地址的元素无法定位， 所以选择点击坐标定位
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id=\"com.manboker.headportrait:id/address_listview\"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]").click()
        '''
        '''
        self.driver.tap([(41, 343)], 500)
        sleep(1)
        #删除地址
        self.driver.swipe(1078, 159, 500, 159, 1000)
        sleep(1)
        self.driver.find_element_by_name("删除").click()
        #修改收货地址
        address_edit = self.driver.find_element_by_id("com.manboker.headportrait:id/address_edit")
        address_edit.click()
        sleep(1)
        edit_address = self.driver.find_element_by_id("com.manboker.headportrait:id/consignee_address_detail_tag")
        edit_address.click()
        edit_address.send_keys("addaddress")
        self.driver.find_element_by_name("保存").click()
        sleep(1)
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback")
        sleep(1)

'''
        #接受新消息通知
        for i in range(1,3):
            accept_mns = self.driver.find_element_by_id("com.manboker.headportrait:id/set_notification_turn")
            accept_mns.click()
            sleep(1)

        #
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(aboutComic)
    unittest.TextTestRunner(verbosity=2).run(suite)