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

    def tearDown(self):
        self.driver.quit()

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
        self.driver.flick(128, 202, 394, 424) #滑动背景图
        confirm.click()
        #点击保存分享， 防止相册无图的情况
        self.driver.find_element_by_name("保存/分享").click()
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name("定制"))
        self.driver.find_element_by_id("com.manboker.headportrait:id/comic_save_goback").click()  #返回， 此时相册中存有背景图

        #选背景
        self.driver.find_element_by_name("选背景").click()  # 进入选背景
        self.driver.find_element_by_id("android.widget.RelativeLayout").click() #选择第一个相册
        self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-id=\"com.manboker.headportrait:id/child_image\"]").click()
        confirm.click()
        self.driver.find_element_by_name("编辑").click()
        common.tap(self)  # 滑动背景图
        confirm.click()
        self.driver.find_element_by_name("保存/分享").click() #点击保存分享
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name("定制"))
        #返回到主界面
        self.driver.find_element_by_id("com.manboker.headportrait:id/comic_save_goback").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_layout").click()
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
        select_textures = WebDriverWait(self.driver,10).until(lambda x: x.find_element_by_xpath("//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/sign_qp_image\"]/android.widget.RelativeLayout[1]"))
        select_textures.click()
        self.driver.find_element_by_name("浪漫").click()
        select_textures.click()
        self.driver.find_element_by_name("本命猴").click()
        select_textures.click()
        self.driver.find_element_by_name("爱情").click()
        select_textures.click()
        self.driver.find_element_by_name("萌宠").click()
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
                pass

        #保存分享
        self.driver.find_element_by_name("保存/分享").click()  # 点击保存分享
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name("定制"))
        # 返回到主界面
        self.driver.find_element_by_id("com.manboker.headportrait:id/comic_save_goback").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_layout").click()

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

        for i in range(2, 8):
            self.driver.find_element_by_xpath("//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/sign_qp_border\"]/android.widget.RelativeLayout[%d]" %i).click()
            sleep(0.5)


        #添加5个文字气泡
        for n in range (2, 7):
            self.driver.find_element_by_id("com.manboker.headportrait:id/create_text_menu_add").click()
            sleep(1)
            try:
                WebDriverWait(self.driver, 2).until(lambda x: x.find_element_by_name("亲～您添加的气泡已达到上限"))
                print u"亲～您添加的气泡已达到上限"
            except:
                print u'添加的第 %d 个气泡' %n


        '''
        #更改文字颜色
        self.driver.find_element_by_id("com.manboker.headportrait:id/create_text_menu_color").click()
        无法找到元素。。
        for m in range(1, 16):
            self.driver.find_element_by_xpath("//android.widget.HorizontalScrollView/android.view.View[%d]" %m).click()
        '''

        #更改文本显示的格式
        self.driver.find_element_by_id("com.manboker.headportrait:id/create_text_menu_align").click()
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
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name("定制"))

        # 返回到主界面
        self.driver.find_element_by_id("com.manboker.headportrait:id/comic_save_goback").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
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
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath("//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/sign_full_gif\"]/android.widget.RelativeLayout[2]")).click() #选择背景图
        sleep(5)
        self.driver.find_element_by_xpath(
            "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/sign_full_gif\"]/android.widget.RelativeLayout[1]").click()
        sleep(1)
        self.driver.find_element_by_xpath(
            "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/sign_full_gif\"]/android.widget.RelativeLayout[3]").click()
        sleep(5)
        # 保存分享
        self.driver.find_element_by_name("保存/分享").click()  # 点击保存分享
        WebDriverWait(self.driver,20).until(lambda x: x.find_element_by_name("定制"))

        # 返回到主界面
        self.driver.find_element_by_id("com.manboker.headportrait:id/comic_save_goback").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_layout").click()
        sleep(3)

        print u"-----添加动态背景图检查完毕-----"

    def testBrush(self):
        '''
        画笔详情功能
        1. 涂鸦后撤销操作， 撤销操作后的操作
        2. 清空涂鸦
        3. 涂鸦粗细调节， 透明多调节
        4. 全屏涂鸦
        :return:
        '''
        self.driver.find_element_by_id("com.manboker.headportrait:id/create_sign").click()  #进入画笔
        #画笔涂鸦
        self.driver.swipe(350, 600, 850, 600, 500)
        self.driver.swipe(450, 600, 950, 600, 500)
        #取色器
        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_pen_tool_straw").click()   #点击取色器
        self.driver.swipe(250, 600, 750, 600, 1500)
        self.driver.swipe(350, 600, 850, 600, 1500)
        self.driver.swipe(450, 600, 950, 600, 1500)
        #橡皮擦
        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_pen_tool_eraser").click()   #点击橡皮擦
        self.driver.swipe(250, 600, 750, 600, 500)
        self.driver.swipe(350, 600, 850, 600, 500)
        self.driver.swipe(450, 600, 950, 600, 500)

        #向前撤销操作
        for i in range(0, 6):
            self.driver.find_element_by_id("com.manboker.headportrait:id/sign_pen_operation_undo").click()
            sleep(0.5)
        #向后撤销操作
        for m in range(0, 6):
            self.driver.find_element_by_id("com.manboker.headportrait:id/sign_pen_operation_redo").click()
            sleep(0.5)

        #涂鸦后删除(调节粗细和透明度)
        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_pen_tool_pen").click()  #选择画笔
        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_pen_operation_up_down").click()  #隐藏工具栏
        sleep(2)
        self.driver.swipe(220, 350, 220, 850, 500)
        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_pen_up").click()  #打开工具栏
        sleep(1)
        self.driver.tap([(100, 1698)], 500)     #调节画笔粗细
        self.driver.tap([(1075, 1698)], 500)        #调节透明度
        self.driver.swipe(420, 350, 420, 850, 500)
        self.driver.tap([(450, 1698)], 500)  # 调节画笔粗细
        self.driver.tap([(730, 1698)], 500)  # 调节透明度
        self.driver.swipe(620, 350, 620, 850, 500)
        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_pen_operation_clear").click()  #清除所有操作
        self.driver.find_element_by_name("确定").click()      #确认删除所有操作

        #调色板
        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_pen_tool_pick_color").click()     #点击打开调色板
        select_color = self.driver.find_elements_by_class_name("android.view.View")     #选择颜色
        select_color[4].click()
        self.driver.find_element_by_xpath("//android.view.View[@resource-id=\"com.manboker.headportrait:id/old_color_view\"]") #切换为原始颜色
        self.driver.find_element_by_id("com.manboker.headportrait:id/color_picker_close_btn").click()       #关闭调色板
        self.driver.swipe(250, 600, 750, 600, 1500)
        self.driver.swipe(350, 600, 850, 600, 1500)
        self.driver.swipe(450, 600, 950, 600, 1500)
        self.driver.find_element_by_id("com.manboker.headportrait:id/sign_pen_done").click()    #点击确认

        # 保存分享
        self.driver.find_element_by_name("保存/分享").click()  # 点击保存分享
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_name("定制"))
        #返回到主界面
        self.driver.find_element_by_id("com.manboker.headportrait:id/comic_save_goback").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/set_goback").click()
        self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_layout").click()
        sleep(3)

        print u"-----添加画笔检查完毕-----"


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(CreateComic)
    unittest.TextTestRunner(verbosity=2).run(suite)