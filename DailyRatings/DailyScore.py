#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from appium import webdriver
from time import sleep
import os
import Desired_Capabilities

"""
    每日评分,由于是H5 需要Xpath定位元素
"""

#Return ads path relative to this file not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class DailyRating(unittest.TestCase):

    desired_caps = Desired_Capabilities.startdevices()
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print u'设备配置成功'
    sleep(5)

    entity_score = driver.find_element_by_id("com.manboker.headportrait:id/entity_score")
    entity_score.click()
    sleep(5)

    if(driver.current_activity == '.set.activity.RatingActivity'):
        print 'w'
        join_review = driver.find_element_by_xpath("//*[@id='button'][@class='button]")
        print 'w'
        join_review.click()
        print 'w'
        sleep(2)
        print 'w'
    else:
        print u'今日您已评过分---'
        sleep(5)
        driver.quit()

    #查看评分标准
    grading = driver.find_element_by_name("评分标准")
    grading.click()
    sleep(1)

    driver.swipe(500,1410,500,700,1000)*4



