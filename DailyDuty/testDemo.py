# -*- coding:utf-8 -*-
from selenium import webdriver
from appium import webdriver
import unittest
from time import sleep
import Desired_Capabilities
from selenium.webdriver.support.ui import WebDriverWait
import os
import AppException

import common
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

    def testActivitiesContent(self):
        #进入社区首页
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[3].click()
        sleep(8)

        #检查活动的详情内容
        item_content = self.driver.find_elements_by_id("com.manboker.headportrait:id/topic_item_content")
        item_content[1].click()
        sleep(5)

        #检测当前界面是否打开了活动详情
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

        #查看热门活动和关注
        list_hot = self.driver.find_element_by_name("热门")
        list_hot.click()
        sleep(3)
        list_follow = self.driver.find_element_by_name("关注")
        list_follow.click()
        sleep(3)

        #发表漫画
        content_join = self.driver.find_element_by_name("我要参与")
        content_join.click()
        sleep(1)
        topic_comic = self.driver.find_element_by_name("漫画")
        topic_comic.click()
        sleep(8)

        AppException.DefineException().exceptionStartHead()

        view_to_ok = self.driver.find_element_by_name("确定")
        view_to_ok.click()
        sleep(3)

        editmessagetext = self.driver.find_element_by_id("com.manboker.headportrait:id/sendmessage_editmessagetext")
        editmessagetext.send_keys("Beautiful commic")
        sleep(2)
        content_add = self.driver.find_element_by_name("发布")
        content_add.click()
        sleep(4)
        try:
            common.wait_appear_by_id(self, "com.manboker.headportrait:id/item_controller_cachedimageview",3)
            print u'发表漫画赠送两魔豆'

        except:
            print u'未检测出发表漫画赠送两魔豆'

        #点赞
        self.driver.tap([(1003,1696),(1068,1731)],500)

        try:
            common.wait_appear_by_id(self, "com.manboker.headportrait:id/item_controller_cachedimageview",3)
            print u'点赞漫画赠送两魔豆'
        except:
            print u"未检测出点赞漫画赠送两魔豆"

        print u'-----社区活动相关功能检查完成-----（PASS）'

        #返回
        goback = self.driver.find_element_by_id("com.manboker.headportrait:id/topiccontent_goback")
        goback.click()
        sleep(2)

        go_home = self.driver.find_element_by_id("com.manboker.headportrait:id/topic_goback")
        go_home.click()
        sleep(2)

    def testAboutMe(self):
        #进入社区首页
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[3].click()
        sleep(8)

        #检查活动的详情内容
        item_content = self.driver.find_elements_by_id("com.manboker.headportrait:id/topic_item_content")
        item_content[1].click()
        sleep(5)

        #检测当前界面是否打开了活动详情
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

        #点击头像进入个人空间
        user_icon = self.driver.find_element_by_id("com.manboker.headportrait:id/topiccontent_user_icon")
        user_icon.click()
        sleep(3)

        #关注好友
        head_follow = self.driver.find_element_by_id("com.manboker.headportrait:id/head_follow")
        head_follow.click()
        sleep(2)

        #点赞
        try:

            praise_image = self.driver.find_element_by_id("com.manboker.headportrait:id/topic_praise_image")
            praise_image.click()
            sleep(2)
        except:
            print u"检查是否已点上赞"

        #在好友空间里聊天
        head_chat = self.driver.find_element_by_id("com.manboker.headportrait:id/head_chat")
        head_chat.click()
        sleep(1)
        et_edittext = self.driver.find_element_by_id("com.manboker.headportrait:id/et_edittext")
        et_edittext.send_keys("I love moman")
        sleep(1)
        et_ok = self.driver.find_element_by_name("发送")
        et_ok.click()
        sleep(1)

        #给好友发送漫画图片
        send_text_addpic = self.driver.find_element_by_id("com.manboker.headportrait:id/customer_service_send_text_addpic")
        send_text_addpic.click()
        send_text_content_pic = self.driver.find_element_by_id("com.manboker.headportrait:id/e_customer_send_text_content_pic")
        send_text_content_pic.click()
        sleep(1)
        child_checkbox = self.driver.find_element_by_id("com.manboker.headportrait:id/child_checkbox")
        child_checkbox.click()
        sleep(1)
        imagescan_addpic = self.driver.find_element_by_id("com.manboker.headportrait:id/imagescan_addpic")
        imagescan_addpic.click()
        sleep(1)
        #发送拍照图片
        content_camera = self.driver.find_element_by_id("com.manboker.headportrait:id/e_customer_send_text_content_camera")
        content_camera.click()
        sleep(2)
        shutter_button = self.driver.find_element_by_id("com.android.camera2:id/shutter_button")
        shutter_button.click()
        '''
        选择不给用户发送自己拍摄时候的照片
        btn_done = self.driver.find_element_by_id("com.android.camera2:id/btn_done")
        btn_done.click()
        sleep(1)
        '''
        btn_cancel = self.driver.find_element_by_id("com.android.camera2:id/btn_cancel")
        btn_cancel.click()
        sleep(1)

        #下滑查看历史消息
        self.driver.swipe(1100, 400, 1100, 1300, 1000)

        #返回
        close_conversation = self.driver.find_element_by_id("com.manboker.headportrait:id/e_ecommerce_close_conversation")
        close_conversation.click()
        sleep(2)

        #添加好友到黑名单
        set_more = self.driver.find_element_by_id("com.manboker.headportrait:id/specific_user_set_more")
        set_more.click()
        blacklist_text = self.driver.find_element_by_name("加入黑名单")
        blacklist_text.click()
        sleep(1)
        button1 = self.driver.find_element_by_name("确定")
        button1.click()
        sleep(1)
        #移除黑名单
        set_more.click()
        self.driver.find_element_by_name("移出黑名单").click()
        sleep(1)

        print u'-----用户空间检查完成-----（PASS）'

        #返回
        user_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/topic_specific_user_goback")
        user_goback.click()
        sleep(1)

        goback = self.driver.find_element_by_id("com.manboker.headportrait:id/topiccontent_goback")
        goback.click()
        sleep(2)

        go_home = self.driver.find_element_by_id("com.manboker.headportrait:id/topic_goback")
        go_home.click()
        sleep(2)

    def testPostDetails(self):
        '''
        帖子详情界面， 操作点赞、评论、查看发布的图片
        :return:
        '''
        #进入社区首页
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[3].click()
        sleep(8)

        #检查活动的详情内容
        item_content = self.driver.find_elements_by_id("com.manboker.headportrait:id/topic_item_content")
        item_content[1].click()
        sleep(5)

        #检测当前界面是否打开了活动详情
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

        #进入帖子详情
        self.driver.tap([(200, 275), (400, 475)], 500)


        sleep(3)

        #对图片进行放大、滑动查看操作
        show_pic = self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-id=\"com.manboker.headportrait:id/community_comment_show_pic_iv\"]")
        show_pic.click()
        sleep(1)
        for i in range(0,10):
            self.driver.swipe(1150, 900, 500, 900, 1000)
        image_view = self.driver.find_element_by_xpath("//android.widget.ImageView")
        image_view.click()
        sleep(1)

        #添加好友、点赞、评论等操作、赞过的人
        detail_follow = self.driver.find_element_by_id("com.manboker.headportrait:id/detail_follow")
        detail_follow.click()
        sleep(1)
        praise_layout = self.driver.find_element_by_name("赞")
        praise_layout.click()
        sleep(1)

        item_comtv = self.driver.find_element_by_name("评论")
        item_comtv.click()
        sleep(1)
        item_comtv.send_keys("i love moman")
        community_et_ok = self.driver.find_element_by_name("发送")
        community_et_ok.click()
        sleep(2)

        try:
            praisetv_count = self.driver.find_element_by_id("com.manboker.headportrait:id/topic_comment_praisetv_count")
            praisetv_count.click()
            sleep(1)
            for n in range(0,3):
                paise_list_fans_image = self.driver.find_element_by_id("com.manboker.headportrait:id/paise_list_fans_image")
                paise_list_fans_image.click()
                sleep(2)
        except:
            pass

        print u'-----社区帖子详情检查完成-----（PASS）'

        # 返回
        list_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/topic_paise_list_goback")
        list_goback.click()
        sleep(1)
        comment_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/topic_comment_goback")
        comment_goback.click()
        sleep(1)
        topiccontent_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/topiccontent_goback")
        topiccontent_goback.click()
        sleep(1)
        go_home = self.driver.find_element_by_id("com.manboker.headportrait:id/topic_goback")
        go_home.click()
        sleep(2)

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
        sleep(2)
        self.driver.find_element_by_name("清空私聊消息列表").click()
        self.driver.find_element_by_name("确定").click()
        sleep(2)
        self.driver.find_element_by_name("清空我消息列表").click()
        self.driver.find_element_by_name("确定").click()
        sleep(2)
        self.driver.find_element_by_name("清空所有消息列表").click()
        self.driver.find_element_by_name("确定").click()
        sleep(2)

        #返回再次查看所有消息是否已被清除
        notification_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/community_notification_goback")
        notification_goback.click()
        self.driver.find_element_by_name("私聊").click()
        self.driver.find_element_by_name("我").click()

        print u'-----社区系统消息检查完成-----（PASS）'
        #返回
        notification_goback.click()
        #返回首页
        go_home = self.driver.find_element_by_id("com.manboker.headportrait:id/topic_goback")
        go_home.click()
        sleep(2)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(aboutComic)
    unittest.TextTestRunner(verbosity=2).run(suite)