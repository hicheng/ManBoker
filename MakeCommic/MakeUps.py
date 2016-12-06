# -*- coding:utf-8 -*-
from appium import webdriver
import unittest
from PublicResour import Desired_Capabilities
from time import sleep
from PublicResour import common
from selenium.webdriver.support.ui import WebDriverWait

'''
测试美妆界面
1. 测试手机为蓝魔，如果是小屏手机则要改规律
'''


class MakeUpsComic(unittest.TestCase):
    def setUp(self):
        desired_caps = Desired_Capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print u"设备配置成功"
        sleep(10)
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[0].click()
        sleep(8)
        self.driver.find_element_by_name("美妆").click()  # 进入创作
        sleep(10)

    def tearDown(self):
        self.driver.quit()


    def testChangeFace_Eyes_Beard(self):
        '''
        1. 改变脸型，包括成人、儿童、婴儿
        2. 每种脸型遍历一遍
        3. 换眼睛类型
        4. 换胡子
        :return:
        '''
        self.driver.find_element_by_id("com.manboker.headportrait:id/select_face_fl").click()  # 打开脸型选择
        select_face = WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
            "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[1]"))
        select_face.click()
        # 成人
        try:
            for adult in range(2, 11):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % adult).click()
                sleep(1)
        except:
            print u'换成人脸型时可能网速不好，请检查异常'

        # 儿童
        self.driver.find_element_by_name("儿童").click()  # 切换到儿童
        select_face.click()
        try:
            for child in range(2, 10):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % child).click()
                sleep(1)
        except:
            print u'换儿童脸型时可能网速不好，请检查异常'

        # 婴儿
        self.driver.find_element_by_name("婴儿").click()  # 切换到婴儿
        select_face.click()
        try:
            for baby in range(2, 7):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % baby).click()
                sleep(1)
        except:
            print u'换婴儿脸型时可能网速不好，请检查异常'

        # 换眼睛类型
        self.driver.find_element_by_id("com.manboker.headportrait:id/select_pupil_fl").click()  # 打开选择眼睛类型
        select_face.click()
        try:
            for pupil in range(2, 11):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % pupil).click()
                sleep(1)
        except:
            print u'换眼睛类型时可能网速不好，请检查异常'
        select_face.click()  # 去掉美瞳效果

        # 换胡子类型
        self.driver.find_element_by_id("com.manboker.headportrait:id/select_beard_fl").click()  # 打开选择胡子类型
        select_face.click()
        try:
            for beard in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % beard).click()
                sleep(1)
        except:
            print u'换胡子类型时可能网速不好，请检查异常'
        select_face.click()  # 去掉胡子效果

        # 点击确认
        self.driver.find_element_by_name("确定").click()
        sleep(2)
        self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_layout").click()
        sleep(3)

        print u"-----换脸型、美瞳、胡子检查完毕-----"


    def testChangeSkin_Glasses_Eyebrow_SmilingFace_Decoration(self):
        '''
        1. 包含换肤色、眼镜、眉毛、笑脸、头戴和耳戴装饰
        :return:
        '''
        # 换肤色
        self.driver.find_element_by_id("com.manboker.headportrait:id/select_skin_fl").click()  # 打开换肤色
        select_skin = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[1]"))
        select_skin.click()
        self.driver.find_element_by_xpath(
            "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[2]").click()
        self.driver.find_element_by_xpath(
            "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[3]").click()

        # 换眼镜
        self.driver.find_element_by_id("com.manboker.headportrait:id/select_glasses_fl").click()
        select_face = WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
            "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[1]"))
        select_face.click()
        try:
            for glasses in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % glasses).click()
                sleep(1)
        except:
            print u'换眼镜类型时可能网速不好，请检查异常'
        select_face.click()  # 去掉眼镜效果

        # 换眉毛
        self.driver.find_element_by_id("com.manboker.headportrait:id/select_eyebows_fl").click()
        select_face.click()
        try:
            for eyebows in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % eyebows).click()
                sleep(1)
        except:
            print u'换眉毛类型时可能网速不好，请检查异常'
        select_face.click()  # 去掉眉毛效果

        # 换笑脸
        self.driver.find_element_by_id("com.manboker.headportrait:id/select_expression_fl").click()
        select_face.click()
        try:
            for expression in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % expression).click()
                sleep(1)
        except:
            print u'换笑脸类型时可能网速不好，请检查异常'
        select_face.click()  # 去掉笑脸效果

        # 头戴发饰
        self.driver.find_element_by_id("com.manboker.headportrait:id/select_hair_accessories_fl").click()
        select_face.click()
        try:
            for accessories in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % accessories).click()
                sleep(1)
        except:
            print u'换头戴发饰类型时可能网速不好，请检查异常'
        select_face.click()  # 去掉头戴发饰效果

        # 换耳戴装饰
        self.driver.find_element_by_id("com.manboker.headportrait:id/select_earring_fl").click()
        select_face.click()
        try:
            for earring in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % earring).click()
                sleep(1)
        except:
            print u'换耳戴装饰类型时可能网速不好，请检查异常'
        select_face.click()  # 去掉耳戴装饰效果

        # 点击确认
        self.driver.find_element_by_name("确定").click()
        sleep(2)
        self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_layout").click()
        sleep(3)

        print u"-----肤色、眼镜、眉毛、笑脸、头戴和耳戴装饰检查完毕-----"


    def testChangeHair(self):
        '''
        换当前界面的所有发型， 不做滑动出现更多种类的处理
        :return:
        '''
        # 换肤色

        self.driver.find_element_by_id("com.manboker.headportrait:id/select_hair_fl").click()  # 打开换肤色
        select_hair = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[1]"))
        select_hair.click()

        # 换头发颜色
        self.driver.find_element_by_id("com.manboker.headportrait:id/btn_change_hair_colors").click()  # 换头发颜色
        try:  # 尝试换肤色
            for haircolors in range(0, 6):
                hair_color = self.driver.find_elements_by_id("com.manboker.headportrait:id/color_item")
                hair_color[haircolors].click()
                sleep(0.5)
        except:
            print u'换肤色失败'

        # 推荐类型
        try:
            for Suggest in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % Suggest).click()
                sleep(1)
        except:
            print u'发型推荐类型可能网速不好，请检查异常'
        # 短发
        self.driver.find_element_by_name("短发").click()
        select_hair.click()
        try:
            for shorthair in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % shorthair).click()
                sleep(1)
        except:
            print u'换短发类型时可能网速不好，请检查异常'
        # 长发
        self.driver.find_element_by_name("长发").click()
        select_hair.click()
        try:
            for longhair in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % longhair).click()
                sleep(1)
        except:
            print u'换长发类型时可能网速不好，请检查异常'
        # 卷发
        self.driver.find_element_by_name("卷发").click()
        select_hair.click()
        try:
            for curls in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % lcurls).click()
                sleep(1)
        except:
            print u'换卷发类型时可能网速不好，请检查异常'
        # 辫子
        self.driver.find_element_by_name("辫子").click()
        select_hair.click()
        try:
            for braid in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % braid).click()
                sleep(1)
        except:
            print u'换辫子类型时可能网速不好，请检查异常'
        # 儿童
        self.driver.find_element_by_name("儿童").click()
        select_hair.click()
        try:
            for child in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % child).click()
                sleep(1)
        except:
            print u'换儿童类型时可能网速不好，请检查异常'
        # 古装
        self.driver.find_element_by_name("古装").click()
        select_hair.click()
        try:
            for costume in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % costume).click()
                sleep(1)
        except:
            print u'换古装类型时可能网速不好，请检查异常'
        # 民族
        self.driver.find_element_by_name("民族").click()
        select_hair.click()
        try:
            for nation in range(2, 13):
                self.driver.find_element_by_xpath(
                    "//it.sephiroth.android.library.widget.HListView[@resource-id=\"com.manboker.headportrait:id/dress_gallery_dr\"]/android.widget.RelativeLayout[%d]" % nation).click()
                sleep(1)
        except:
            print u'换民族类型时可能网速不好，请检查异常'

        # 点击确认
        self.driver.find_element_by_name("确定").click()
        sleep(2)
        self.driver.find_element_by_id("com.manboker.headportrait:id/comics_main_layout").click()
        sleep(3)

        print u"-----换发型和发色检查完毕-----"

    '''
def testZoom(self):

    美妆缩放界面
    :return:

    WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_name("150%")).click()
    self.driver.pinch("com.manboker.headportrait:id/dressing_goback")  # 缩小
    self.driver.zoom(629, 815)     #放大
    '''


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MakeUpsComic)
    unittest.TextTestRunner(verbosity=2).run(suite)