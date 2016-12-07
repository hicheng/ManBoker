# -*- coding:utf-8 -*-
from selenium import webdriver
from appium import webdriver
import unittest
from time import sleep
from PublicResour import Desired_Capabilities
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
        self.driver.implicitly_wait(10)

        print u'设备配置成功'
        sleep(10)

    def testSetting(self):

        #进入我的
        head_icon = self.driver.find_element_by_id("com.manboker.headportrait:id/entry_album_set_icon")
        head_icon.click()


        #点击进入设置界面
        set_general = self.driver.find_element_by_name("设置")
        set_general.click()


        #管理黑名单
        set_blacklist = self.driver.find_element_by_name("黑名单管理")
        set_blacklist.click()

        #如果list下存在黑名单的情况
        try:
            list_head = self.driver.find_element_by_id("com.manboker.headportrait:id/paise_list_head")
            list_head.click()

            set_more = self.driver.find_element_by_id("com.manboker.headportrait:id/specific_user_set_more")
            set_more.click()
            self.driver.find_element_by_name("移出黑名单").click()

            self.driver.find_element_by_id("com.manboker.headportrait:id/topic_specific_user_goback").click()

            self.driver.swipe(1110, 378, 1110, 1000, 1000)

            self.driver.find_element_by_id("com.manboker.headportrait:id/topic_paise_list_goback").click()

        except:
            self.driver.find_element_by_id("com.manboker.headportrait:id/topic_paise_list_goback").click()



        #收货地址管理
        set_receive_adress = self.driver.find_element_by_name("收货地址管理")
        set_receive_adress.click()

        #添加两个收货地址
        for n in range(1,3):
            self.driver.find_element_by_id("com.manboker.headportrait:id/new_address").click()

            #选择省市区,默认北京市东城区
            self.driver.find_element_by_name("省、市、区").click()

            self.driver.find_element_by_name("确定").click()
            #填写详细地址
            address_detail = self.driver.find_element_by_name("详细地址")
            address_detail.click()
            address_detail.send_keys("Testaddress")

            #填写联系人
            consignee_name = self.driver.find_element_by_name("收货人姓名")
            consignee_name.click()
            consignee_name.send_keys("Testname")
            #填写手机号码（暂时未确认手机号码的区号）
            consignee_phonenumber = self.driver.find_element_by_name("手机号码")
            consignee_phonenumber.click()
            consignee_phonenumber.send_keys("13000000000")
            self.driver.find_element_by_name("保存").click()


        #更换默认地址

        '''
        因为更改默认收货地址的元素无法定位， 所以选择点击坐标定位
        self.driver.find_element_by_xpath("//android.widget.ListView[@resource-id=\"com.manboker.headportrait:id/address_listview\"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]").click()
        '''


        self.driver.tap([(41, 343)], 500)

        #删除地址
        self.driver.swipe(1078, 159, 500, 159, 1000)

        self.driver.find_element_by_name("删除").click()
        #修改收货地址
        address_edit = self.driver.find_element_by_id("com.manboker.headportrait:id/address_edit")
        address_edit.click()

        edit_address = self.driver.find_element_by_id("com.manboker.headportrait:id/consignee_address_detail_tag")
        edit_address.click()
        edit_address.send_keys("addaddress")
        self.driver.find_element_by_name("保存").click()

        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()



        #接受新消息通知
        for i in range(0, 2):
            accept_mns = self.driver.find_element_by_id("com.manboker.headportrait:id/set_notification_turn")
            accept_mns.click()



        #问题与帮助(查看其中一个问题内容， 检测内容是否加载出来)
        set_faq = self.driver.find_element_by_name("问题与帮助")
        set_faq.click()
        sleep(2)
        self.driver.find_element_by_id("com.manboker.headportrait:id/web_back_btn").click()
        sleep(2)


        #意见反馈
        self.driver.find_element_by_name("意见反馈").click()
        sleep(2)
        Feedback_type = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"意见反馈类型 Link\"]")
        Feedback_type.click()
        sleep(1)
        self.driver.tap([(1150, 1496), (1161, 1492)], 1000)
        sleep(2)
        self.driver.find_element_by_name("增加特效").click()
        self.driver.find_element_by_name("打包下载").click()
        self.driver.find_element_by_name("图片储存").click()
        self.driver.find_element_by_name("调整发色").click()
        sleep(1)
        set_feedback = self.driver.find_element_by_name("意见反馈")
        set_feedback.click()
        sleep(3)
        Feedback = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"Feedback\"]/android.widget.EditText[1]")
        Feedback.click()
        Feedback.send_keys("no Feedback")
        sleep(1)
        Feedback_email = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"Feedback\"]/android.view.View[4]/android.widget.EditText[1]")
        Feedback_email.click()
        Feedback_email.send_keys("my@qq.com")
        sleep(1)
        Link = self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"提交 Link\"]")
        Link.click()
        sleep(3)


        #关于魔漫相机
        adout_moman = self.driver.find_element_by_name("关于魔漫相机")
        adout_moman.click()
        newfeatures = self.driver.find_element_by_id("com.manboker.headportrait:id/set_newfeatures_tv")
        newfeatures.click()
        sleep(2)
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
        sleep(1)
        #因为访问官网界面没有可以返回到客户端的元素，所以暂不写访问官网case
        terms_of_use = self.driver.find_element_by_name("使用条款")
        terms_of_use.click()
        sleep(3)
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
        sleep(1)
        topic_standard = self.driver.find_element_by_name("活动专区内容规范")
        topic_standard.click()
        sleep(3)
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
        sleep(2)
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_about_goback").click()
        sleep(2)


        #商务合作
        set_bussess = self.driver.find_element_by_name("商务合作")
        set_bussess.click()
        sleep(3)
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
        sleep(2)


        #加入我们
        follow_us = self.driver.find_element_by_name("加入我们")
        follow_us.click()
        sleep(3)
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
        sleep(2)


        #网络检测
        netstate = self.driver.find_element_by_name("网络检测")
        netstate.click()
        element = WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_name("发送报告"))
        element.click()
        net_work_back = self.driver.find_element_by_id("com.manboker.headportrait:id/set_check_net_work_back")
        net_work_back.click()
        sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(aboutComic)
    unittest.TextTestRunner(verbosity=2).run(suite)