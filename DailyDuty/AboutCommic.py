# -*- coding:utf-8 -*-
from selenium import webdriver
from appium import webdriver
import unittest
from time import sleep
import Desired_Capabilities
import os
import AppException

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

    def testAMakeComic(self):
        # 彩蛋
        try:
            news_page_close = self.driver.find_element_by_id("com.manboker.headportrait:id/news_page_close")
            news_page_close.click()
            sleep(3)
        except:
            pass
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[0].click()
        sleep(8)

        AppException.DefineException().exceptionStartHead()
        sleep(1)

        try:
            refresh_comic = self.driver.find_element_by_name("刷新")
            refresh_comic.click()
            print u'-----今日漫画已刷新-----（PASS）'
            sleep(8)
        except:
            print u'今日没有检测出新图， 请检查设备（Fail）'
            pass
            sleep(5)
        try:
            refresh1_comic = self.driver.find_element_by_name("领取")
            refresh1_comic.click()
            print u'-----今日漫画已刷新-----（PASS）'
            sleep(8)
        except:
            print u'今日没有检测出新图， 请检查设备（Fail）'
            pass
            sleep(5)

        AppException.DefineException().exceptionStartHead()
        sleep(2)

        #向右滑动显示明日刷新时间
        self.driver.swipe(300,900,1000,900,3000)

        try:
            self.driver.find_element_by_name("00:00:00")
            print u'明日更新的时间为00:00:00'
        except:
            print u'-----精彩魔图 即将更新-----（PASS）'
            pass

        AppException.DefineException().exceptionStartHead()
        sleep(2)

        #向左滑动显示更新的第二张图片
        self.driver.swipe(1150,900,500,900,1000)
        #又下角可能会出现魔豆icon
        sleep(3)
        try:
            modouicon = self.driver.find_element_by_name('美妆可以让你的角色更好看~')
            modouicon.click()
        except:
            pass
        sleep(5)

        AppException.DefineException().exceptionStartHead()
        sleep(1)

        #收藏漫画
        favorite_comic = self.driver.find_element_by_id("com.manboker.headportrait:id/comic_praise_iv")
        if (favorite_comic.is_selected() == True):
            pass
        else:
            favorite_comic.click()
        sleep(1)
        print u'-----漫画已收藏-----（PASS）'

        #从做漫画返回到首页
        back_makecomic = self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_top_view_to_entry_iv")
        back_makecomic.click()
        print u'-----漫画更新相关功能检查完成-----（PASS）'
        sleep(5)

    def testBackGroundAndSaveShare(self):
        '''
        先拍背景再保存分享
        :return:
        '''
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[0].click()
        sleep(8)

        AppException.DefineException().exceptionStartHead()

        enter_click = self.driver.find_element_by_name("创作")
        enter_click.click()
        sleep(3)
        # 拍背景
        select_background = self.driver.find_element_by_id("com.manboker.headportrait:id/sign_change_bg_layout")
        select_background.click()
        sleep(2)
        background = self.driver.find_element_by_name("拍背景")
        background.click()
        sleep(5)
        back_background = self.driver.find_element_by_id("com.manboker.headportrait:id/change_bg_back_iv")
        back_background.click()
        sleep(2)
        # 保存分享漫画
        save_share = self.driver.find_element_by_name("保存/分享")
        save_share.click()
        sleep(5)
        # 返回下一张漫画拍背景
        save_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/comic_save_goback")
        save_goback.click()
        sleep(1)
        set_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback")
        set_goback.click()
        sleep(2)
        set_goback.click()
        sleep(3)
        '''
            # 向左滑动显示第一张更新的漫画
            self.driver.swipe(300, 900, 1000, 900, 3000)

            AppMethon.DefineMethon().methonBackGroundAndSaveShare()
        '''
        # 从做漫画返回到首页
        back_makecomic = self.driver.find_element_by_id(
            "com.manboker.headportrait:id/comics_main_top_view_to_entry_iv")
        back_makecomic.click()
        print u'-----拍背景和保存分享检查完成-----（PASS）'
        sleep(5)

    def testComicInfoPage(self):
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[0].click()
        sleep(8)

        AppException.DefineException().exceptionStartHead()

        '''
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[0].click()
        sleep(10)
        '''
        commit_btn = self.driver.find_element_by_id("com.manboker.headportrait:id/commit_btn")
        commit_btn.click()
        sleep(5)

        #漫画评分
        try:
            star_rating = self.driver.find_elements_by_class_name("android.widget.ImageView")
            star_rating[3].click()
            sleep(2)
        except:
            print u'点击漫画评分无效果'
        # 打标签
        tag = self.driver.find_element_by_name("加标签")
        tag.click()

        #添加标签后删除标签
        add_tag = self.driver.find_element_by_id("com.manboker.headportrait:id/add_tag_et")
        add_tag.click()
        add_tag.send_keys("addtag")
        self.driver.find_element_by_name("添加").click()
        sleep(1)
        delete_tag = self.driver.find_element_by_name("addtag")
        delete_tag.click()
        sleep(1)
        confirm_delete_tag = self.driver.find_element_by_id("android:id/button1")
        confirm_delete_tag.click()
        sleep(1)
        self.driver.find_element_by_id("com.manboker.headportrait:id/add_tag_btn_back").click()
        sleep(2)

        #添加感受
        sleep(5)
        add_feeling = self.driver.find_element_by_id("com.manboker.headportrait:id/add_feeling_et")
        add_feeling.click()
        add_feeling.send_keys("testfeeling")
        self.driver.find_element_by_id("com.manboker.headportrait:id/comic_add_feeling_btn").click()
        sleep(5)

        favorite = self.driver.find_element_by_id("com.manboker.headportrait:id/comit_praise_btn")
        favorite.click()
        sleep(2)
        title_hot = self.driver.find_element_by_id("com.manboker.headportrait:id/comic_info_comit_title_hot_btn")
        title_hot.click()
        sleep(1)

        #下拉界面刷新感受
        self.driver.swipe(1137, 450, 1137, 649, 1000)
        sleep(1)

        self.driver.find_element_by_id("com.manboker.headportrait:id/comic_info_btn_back").click()
        sleep(5)

        AppException.DefineException().exceptionStartHead()

        # 从做漫画返回到首页
        back_makecomic = self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_top_view_to_entry_iv")
        back_makecomic.click()
        print u'-----漫画信息页检查完成-----（PASS）'
        sleep(5)

    def testMomicMall(self):

        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[0].click()
        sleep(8)

        AppException.DefineException().exceptionStartHead()

        #进入魔豆商城
        beanmall = self.driver.find_element_by_id("com.manboker.headportrait:id/bean")
        beanmall.click()
        sleep(5)

        #购买漫画
        self.driver.tap([(22,231),(402,771)],500)
        sleep(5)
        md_detail = self.driver.find_element_by_id("com.manboker.headportrait:id/md_detail_purchase")
        md_detail.click()
        sleep(2)
        # 没有考虑魔豆数量足的情况， 因为我们的魔豆根本不够用啊！！
        try:
            button = self.driver.find_element_by_name("我知道了")
            print u'魔豆数量不足'
            button.click()
            sleep(2)
        except:
            pass
        set_goback = self.driver.find_element_by_id("com.manboker.headportrait:id/set_go_back")
        set_goback.click()
        sleep(2)
        purchased = self.driver.find_element_by_name("已购图")
        purchased.click()
        sleep(8)

        AppException.DefineException().exceptionStartHead()

        # 从做已购图分类返回到首页
        back_makecomic = self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_top_view_to_entry_iv")
        back_makecomic.click()
        print u'-----魔豆商城检查完成-----（PASS）'
        sleep(5)

    def testChangeComplexion(self):
        '''
        :return: 美妆更改漫画肤色
        '''
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[0].click()
        sleep(8)

        AppException.DefineException().exceptionStartHead()

        #进入美妆
        enter_faceedit = self.driver.find_element_by_name("美妆")
        enter_faceedit.click()
        sleep(5)
        #选择皮肤
        click_edit = self.driver.find_element_by_id("com.manboker.headportrait:id/select_skin_btn")
        click_edit.click()
        sleep(3)
        #换肤色
        self.driver.tap([(204, 1697), (272, 1765)], 500)
        sleep(2)
        self.driver.tap([(109,1697),(177,1765)],500)
        sleep(2)
        self.driver.tap([(14, 1697), (82, 1765)], 500)
        sleep(2)
        #返回
        cancel_back = self.driver.find_element_by_id("com.manboker.headportrait:id/dress_cancel_back")
        cancel_back.click()
        sleep(1)
        button = self.driver.find_element_by_name("保存")
        button.click()
        sleep(3)

        AppException.DefineException().exceptionStartHead()

        # 从做漫画返回到首页
        back_makecomic = self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_top_view_to_entry_iv")
        back_makecomic.click()
        print u'-----美妆改肤色检查完成-----（PASS）'
        sleep(5)

    def testSearchKeyword(self):
        '''

        :return: 搜索漫画
        '''
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[0].click()
        sleep(8)

        AppException.DefineException().exceptionStartHead()

        # 进入搜索漫画界面
        click_search = self.driver.find_element_by_id(
            "com.manboker.headportrait:id/comics_main_top_view_to_search_iv")
        click_search.click()
        sleep(3)
        # 点击搜索
        search_comic = self.driver.find_element_by_name("搜索")
        search_comic.click()
        sleep(8)

        AppException.DefineException().exceptionStartHead()

        # 从做漫画返回到首页
        back_makecomic = self.driver.find_element_by_id(
            "com.manboker.headportrait:id/comics_main_top_view_to_entry_iv")
        back_makecomic.click()
        print u'-----漫画搜索检查完成-----（PASS）'
        sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(aboutComic)
    unittest.TextTestRunner(verbosity=2).run(suite)
