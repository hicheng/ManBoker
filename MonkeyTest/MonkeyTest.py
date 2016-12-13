# coding: UTF-8

import os
import sys


#os.popen("adb shell monkey -p com.manboker.headportrait --throttle 300 -s 100 -v -v 50| tee log.log")

print open(sys.path[0] + "\log.log","r").read()