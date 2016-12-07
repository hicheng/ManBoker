# -*- coding:UTF-8 -*-

import time
#已登录账号
class PersonalInfo(object):
    def enterMine(self):
        # 点击头像
        click_photo = self.driver.find_element_by_id("com.manboker.headportrait:id/imageView_head")
        click_photo.click()

        #更换头像
        change_photo = self.driver.find_element_by_id("com.manboker.headportrait:id/imageView_head")
        change_photo.click()

        take_picture = self.driver.find_element_by_name("拍照")
        take_picture.click()
        time.sleep(1)
        take_btn = self.driver.find_element_by_id("com.huawei.camera:id/shutter_button")
        take_btn.click()
        time.sleep(1)
        determine = self.driver.find_element_by_id("com.huawei.camera:id/btn_done")
        determine.click()
        select = self.driver.find_element_by_name("获取")
        select.click()

    def change_name(self):
        #点击用户名框
        click_name = self.driver.find_element_by_id("com.manboker.headportrait:id/set_nick_name_RL")
        click_name.click()

