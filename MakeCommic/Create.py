# -*- coding:utf-8 -*-
from appium import webdriver
import unittest
from PublicResour import Desired_Capabilities
from time import sleep
from PublicResour import common
from selenium.webdriver.support.ui import WebDriverWait
'''
测试创作界面
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

        self.driver.find_element_by_name("创作").click()  # 进入创作

    def testShootBackground(self):
        '''
        拍背景，具体详细的功能
        :return:
        '''

        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_change_bg_layout").click() #进入拍背景
        self.driver.find_element_by_name("拍背景").click()  #进入拍背景
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("com.manboker.headportrait:id/change_bg_take_picture")).click() #拍照
        confirm = WebDriverWait(self.driver, 10).until( lambda x: x.find_element_by_name("确定"))
        confirm.click()
        #编辑背景
        self.driver.find_element_by_name("编辑").click()
        common.tap(self) #滑动背景图
        confirm.click()
        #点击保存分享， 防止相册无图的情况
        self.driver.find_element_by_name("保存/分享").click()
        sleep(2)
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()  #返回， 此时相册中存有背景图

        #选背景
        self.driver.find_element_by_name("选背景").click()  # 进入选背景
        self.driver.find_element_by_id("android.widget.RelativeLayout").click() #选择第一个相册
        self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-id=\"com.manboker.headportrait:id/child_image\"]").click()
        confirm.click()
        self.driver.find_element_by_name("编辑").click()
        common.tap(self)  # 滑动背景图
        confirm.click()
        self.driver.find_element_by_name("保存/分享").click() #点击保存分享

        #返回到主界面
        for i in range(0, 3):
            self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
            sleep(1)
        self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_layout").click()
        sleep(3)

        print u"-----拍背景检查完毕-----"

    def testStaticTextures(self):
        '''
        静态贴图
        1. 每个分类加载一个图片
        2. 静态贴图最多添加10个， 超过十个会有上限提示
        :return:
        '''

        #进入静态贴图
        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_qp_image_iv").click()
        #选择所有频道的第一个贴图
        select_textures = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_class_name("android.widget.RelativeLayout"))
        select_textures.click()
        self.driver.find_element_by_name("浪漫").click()
        select_textures.click()
        self.driver.find_element_by_name("本命猴").click()
        select_textures.click()
        self.driver.find_element_by_name("爱情").click()
        select_textures.click()
        self.driver.find_element_by_name("爱萌宠").click()
        select_textures.click()
        self.driver.find_element_by_name("萌物").click()
        select_textures.click()
        self.driver.find_element_by_name("生日快乐").click()
        for i in range(6, 11):
            select_textures.click()
            try:
                self.driver.find_element_by_name("亲～您添加的贴图已达到上限")
                print u"添加了10张图"
            except:
                print '添加了第' + i + '静态图'

        #保存分享
        self.driver.find_element_by_name("保存/分享").click()  # 点击保存分享

        # 返回到主界面
        for i in range(0, 2):
            self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
            sleep(1)
        self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_layout").click()
        sleep(3)

        print u"-----添加静态图检查完毕-----"

    def testTextBubbles(self):
        '''
        1. 文字气泡只能添加一种形式
        2. 添加文字气泡内容后， 切换气泡不改变文字内容
        3. 最多添加5个文字气泡
        :return:
        '''
        #切换文字气泡
        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_qp_border_iv").click()
        for i in range(1, 7):
            select_bubbles = self.driver.find_elements_by_class_name("android.widget.RelativeLayout")
            select_bubbles[i].click()
            sleep(1)

        #添加5个文字气泡
        for n in range (0, 6):
            self.driver.find_element_by_id("com.manboker.headportrait:id/create_text_menu_add").click()
            sleep(1)
            try:
                self.driver.find_element_by_name("亲～您添加的气泡已达到上限")
                print u"添加了5个气泡"
            except:
                print u"添加第"+ n + u"个气泡"

        #更改文字颜色
        self.driver.find_element_by_id("com.manboker.headportrait:id/create_text_menu_color").click()
        for m in range(0, 16):
            select_color = self.driver.find_elements_by_class_name("android.view.View")
            select_color[m].click()

        #更改文本显示的格式
        self.driver.find_element_by_name("居中对齐").click()
        self.driver.find_element_by_name("右对齐").click()
        self.driver.find_element_by_name("左对齐").click()
        self.driver.find_element_by_name("加粗").click()
        self.driver.find_element_by_name("阴影").click()

        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_gif_iv").click()  #显示前50%的透明度
        self.driver.find_element_by_id("com.manboker.headportrait:id/create_sign").click()  #显示后50%的透明度
        self.driver.find_element_by_id("com.manboker.headportrait:id/create_text_menu_confirm").click()  #确认编辑
        # 保存分享
        self.driver.find_element_by_name("保存/分享").click()  # 点击保存分享

        # 返回到主界面
        for i in range(0, 2):
            self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
            sleep(1)
        self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_layout").click()
        sleep(3)

        print u"-----添加文字气泡检查完毕-----"

    def testDynamicBackground(self):
        '''
        添加动态背景图
        1. 可以更换动态背景图
        2. 测试设备切换动图时较卡， 省略多次切图
        :return:
        '''
        #进入动态背景图
        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_full_gif_iv").click()
        select_Dynamic = self.driver.find_elements_by_class_name("android.widget.RelativeLayout") #选择背景图
        select_Dynamic[1].click()
        sleep(5)
        select_Dynamic[0].click()
        sleep(1)
        select_Dynamic[1].click()
        sleep(5)
        # 保存分享
        self.driver.find_element_by_name("保存/分享").click()  # 点击保存分享

        # 返回到主界面
        for i in range(0, 2):
            self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
            sleep(1)
        self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_layout").click()
        sleep(3)

        print u"-----添加动态背景图检查完毕-----"

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(CreateComic)
    unittest.TextTestRunner(verbosity=2).run(suite)