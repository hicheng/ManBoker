# -*- coding:utf-8 -*-
from selenium import webdriver
import urllib2
import time

browser = webdriver.Chrome()

a = browser.get("http://mall.manboker.com/CN?lang=zh&platform=ios&imei=7112C399-17E9-46F4-A03B-12727E715F3D&ver=336&iosVer=10.1.1&userid=37cb361f-ae78-420a-8918-b681ec23d73a&token=1qC3CgvnRoSaEWnrNnUFvvBvi3I_CN")
time.sleep(10)

print browser.page_source