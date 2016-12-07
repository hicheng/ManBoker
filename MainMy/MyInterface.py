#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from appium import webdriver
from time import sleep
import os
from PublicResour import Desired_Capabilities

"""
    登录状态下检查“我的”界面的所有的功能模块
    大部分执行用例时在“我的”界面
"""

#Return ads path relative to this file not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class My(unittest.TestCase):
    def setUp(self):
        desired_caps = Desired_Capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print u'设备配置成功'
        sleep(5)

    def test_myFavorite(self):
        print u'进入首页了----'
        make_commic = self.driver.find_elements_by_class_name("android.view.View")
        make_commic[0].click()
        sleep(5)
        favorite_comic = self.driver.find_element_by_id("com.manboker.headportrait:id/comic_praise_iv")
        if (favorite_comic.is_selected() == True):
            pass
        else:
            favorite_comic.click()
        sleep(1)
        print u'漫画已收藏'

        main_entry = self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_top_view_to_entry_iv")
        main_entry.click()
        sleep(1)
        print u'返回到主界面'

        head_icon = self.driver.find_element_by_id("com.manboker.headportrait:id/entry_album_set_icon")
        head_icon.click()
        sleep(1)

        select_myfavorite =  self.driver.find_element_by_id("com.manboker.headportrait:id/set_favorite_tv")
        select_myfavorite.click()
        sleep(3)
        print u'进入我的收藏'

        edit_favorite = self.driver.find_element_by_id("com.manboker.headportrait:id/edit_iv")
        edit_favorite.click()
        sleep(1)
        item_comic_favorite= self.driver.find_element_by_id("com.manboker.headportrait:id/item_layout_0_iv")
        item_comic_favorite.click()
        sleep(1)
        delete_comic_favorite = self.driver.find_element_by_id("com.manboker.headportrait:id/delete_tv")
        delete_comic_favorite.click()
        sleep(1)
        confirm_delete = self.driver.find_element_by_id("android:id/button1")
        confirm_delete.click()
        sleep(1)
        print u'你已经把漫画删除了， 表情改版没做好暂时不过表情模块'
        back_my = self.driver.find_element_by_id("com.manboker.headportrait:id/iv_back")
        back_my.click()
        sleep(2)

        self.driver.find_element_by_id("com.manboker.headportrait:id/set_set_goback").click()
        sleep(2)

    def test_aboutMe(self):

        head_icon = self.driver.find_element_by_id("com.manboker.headportrait:id/entry_album_set_icon")
        head_icon.click()
        sleep(1)
        print u'进入个人空间'
        select_aboutme = self.driver.find_element_by_name("我的空间")
        select_aboutme.click()
        sleep(3)
        user_headicon = self.driver.find_element_by_id("com.manboker.headportrait:id/specific_user_headicon")
        user_headicon.click()
        sleep(3)
        self.driver.get_screenshot_as_file('C:\Pycharm\Manboker\MainMy\Screenshot\userhead' + '.jpg')
        sleep(1)
        self.driver.find_element_by_id("com.manboker.headportrait:id/community_comment_adjust_imageview").click()
        sleep(1)
        self.driver.swipe(1000,600,1000,900,1000)
        sleep(1)
        self.driver.get_screenshot_as_file('C:\Pycharm\Manboker\MainMy\Screenshot\AboutMe' + '.jpg')
        print u'-----个人空间检查完毕-----'
        go_backmy = self.driver.find_element_by_id("com.manboker.headportrait:id/topic_specific_user_goback")
        go_backmy.click()
        sleep(2)

        self.driver.find_element_by_id("com.manboker.headportrait:id/set_set_goback").click()
        sleep(2)

    def test_myFollowing(self):

        head_icon = self.driver.find_element_by_id("com.manboker.headportrait:id/entry_album_set_icon")
        head_icon.click()
        sleep(1)
        print u'进入我的关注'
        select_myfollowing = self.driver.find_element_by_name("我的关注")
        select_myfollowing.click()
        sleep(2)
        #添加关注
        add_following = self.driver.find_element_by_id("com.manboker.headportrait:id/t_fans_image")
        add_following.click()
        sleep(2)
        #刷新后再次关注好友和取消关注
        self.driver.swipe(1000, 600, 1000, 900, 1000)
        sleep(3)
        add_following.click()
        sleep(2)
        cancel_following = add_following
        cancel_following.click()
        sleep(1)

        find_follows = self.driver.find_element_by_id("com.manboker.headportrait:id/t_follows_find")
        find_follows.click()
        sleep(2)
        #换一换
        refresh_friends = self.driver.find_element_by_name("换一换")
        refresh_friends.click()
        sleep(2)

        add_follow = self.driver.find_element_by_id("com.manboker.headportrait:id/add_follow")
        add_follow.click()
        #返回到我的界面
        self.driver.find_element_by_id("com.manboker.headportrait:id/t_find_back").click()
        sleep(2)
        go_backmy = self.driver.find_element_by_id("com.manboker.headportrait:id/t_follows_back")
        go_backmy.click()
        sleep(2)

        self.driver.find_element_by_id("com.manboker.headportrait:id/set_set_goback").click()
        sleep(2)

    def test_Followers(self):
        head_icon = self.driver.find_element_by_id("com.manboker.headportrait:id/entry_album_set_icon")
        head_icon.click()
        sleep(1)

        print u'进入我的粉丝'
        select_followers = self.driver.find_element_by_name("我的粉丝")
        select_followers.click()
        sleep(2)

        self.driver.swipe(1000, 600, 1000, 900, 1000)
        sleep(2)
        self.driver.swipe(1000, 900, 1000, 600, 1000)
        sleep(2)

        go_backmy = self.driver.find_element_by_id("com.manboker.headportrait:id/topic_paise_list_goback")
        go_backmy.click()

        self.driver.find_element_by_id("com.manboker.headportrait:id/set_set_goback").click()
        sleep(2)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(My)
    unittest.TextTestRunner(verbosity=2).run(suite)
#    unittest.main()


