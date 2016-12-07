# -*- coding:utf-8 -*-
import time
import unittest

from appium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from DailyDuty import AppMethon
from PublicResour import Desired_Capabilities, AppMethon
from PublicResour import common


class TestYangRan(unittest.TestCase):

    def setUp(self):
        desired_caps = Desired_Capabilities.startdevices()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps )

        print u'设备配置成功'
        time.sleep(5)
    def test_testcomic(self):
        # 在本地设置存放截图的文档

        AppMethon.CreateDir('/Screenshot/favorite/')
        AppMethon.CreateDir('/Screenshot/background/')

        #关闭导航界面
        page_close = self.driver.find_element_by_id("com.manboker.headportrait:id/news_page_close")
        page_close.click()

        AppMethon.NormalLogin(self, "18500307774", "yr.0411")

        try:
            home_page = WebDriverWait(self.driver, 2).until(lambda x: x.find_element_by_id("com.manboker.headportrait:id/set_set_goback"))
            home_page.click()
        except:
            pass

        # 进入做漫画界面
        enter_makecomic = self.driver.find_elements_by_class_name("android.view.View")
        enter_makecomic[0].click()

        AppMethon.ShootBackgroundMethon(self)

        #向左滑动
        for i in range(1, 100):
            common.swipe_left(self)
            try:
                WebDriverWait(self.driver, 5).until(
                    lambda x: x.find_element_by_name("点击漫画左下角的收藏按钮即可添加到我的收藏频道"))
                print u"----图已测完， 到了我的收藏界面-----"
                self.driver.quit()
            except:
                print i
            AppMethon.ShootBackgroundMethon(self)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestYangRan)
    unittest.TextTestRunner(verbosity=2).run(suite)







