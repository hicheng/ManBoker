# -*- coding:utf-8 -*-
import os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def startdevices():
    desired_caps = {}
    desired_caps = {}
    desired_caps['deviceName'] = '01234567890123456789'  # adb devices查到的设备名
    desired_caps['platformName'] = 'Android'  # 测试平台名称
    desired_caps['platformVersion'] = '4.4.4'  # 待测手机的系统版本号
    desired_caps['appPackage'] = 'com.manboker.headportrait'  # 被测App的包名
    desired_caps['appActivity'] = '.activities.SplashActivity'  # 打开界面的Activity， 获得appActivity详情见http://www.cnblogs.com/kllay/p/5506480.html
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboard'] = 'True'  # 后两行解决输入法的问题
    desired_caps['newCommandTimeout'] = 120
    return desired_caps