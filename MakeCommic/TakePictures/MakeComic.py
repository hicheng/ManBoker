
# -*- coding:UTF-8 -*-
from selenium import webdriver
import time
#import unittest
import os
# Return ads path relative to this file not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class startDevices(object):
    def start(self):
        desired_caps = {}
        desired_caps['deviceName'] = '01234567890123456789'  # adb devices查到的设备名
        desired_caps['platformName'] = 'Android'    #测试平台名称
        desired_caps['platformVersion'] = '4.4.4'     # 待测手机的系统版本号
        desired_caps['appPackage'] = 'com.manboker.headportrait'  # 被测App的包名
        desired_caps['appActivity'] = '.activities.SplashActivity'    # 打开界面的Activity， 获得appActivity详情见http://www.cnblogs.com/kllay/p/5506480.html
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)
    def close(self):
        self.driver.quit()

    def makeComic(self):
        enter_make_comic = self.driver.find_element_by_class_name('android.view.View')
        enter_make_comic.click()
        time.sleep(2)

    def saveShare(self):
        #保存分享
        save_share = self.driver.find_element_by_id('com.manboker.headportrait:id/comics_main_top_view_to_share_iv')
        save_share.click()
        time.sleep(1)

        #返回到做漫画界面
        back_comic = self.driver.find_element_by_id('com.manboker.headportrait:id/comic_save_goback')
        back_comic.click()
        time.sleep(1)

    def selectPhoto(self):
        take_pictures = self.driver.find_element_by_id('com.manboker.headportrait:id/comics_main_top_view_to_camera_iv')
        take_pictures.click()
        time.sleep(1)
        phone_photo = self.driver.find_element_by_name('手机相册')
        phone_photo.click()
        time.sleep(1)
        #暂时不做上滑查找元素处理

        #！换设备后需要更改
        select_album = self.driver.find_element_by_name('image (98)')
        select_album.click()
        time.sleep(1)

        #选择照片
        select_photo = self.driver.find_element_by_class('android.widget.RelativeLayout')
        select_photo[0].click()


#if __name__ == '__main__':
#    suite = unittest.TestLoader().loadTestsFromTestCase(startDevices)
#    unittest.TextTestRunner(verbosity=2).run(suite)

Moman = startDevices()
Moman.start()
Moman.makeComic()
Moman.saveShare()
Moman.selectPhoto()
Moman.close()
