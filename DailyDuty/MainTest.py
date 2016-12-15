# -*- coding:utf-8 -*-
from DailyDuty import AboutCommic, AboutMomieWorld
from DailyRatings import DailyScore
import time
import unittest
import BSTestRunner

def ExecuteCase():

    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AboutCommic.aboutComic))    # 做漫画
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AboutMomieWorld.aboutMomieWorld))    # 社区
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(DailyScore.dailyScore))     # 每日评分

#    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    filename = "C:\Pycharm\ManBoker\\report.html"
    print (filename)
    fp = open(filename, 'w')
    runner = BSTestRunner.BSTestRunner(
        stream=fp,
        title='Test',
        description='Daily Update Check'
    )
    runner.run(suite)
    fp.close()
if __name__ == "__main__":
    ExecuteCase()