# -*- coding:utf-8 -*-
from LG import HTMLTestRunner_cn
import unittest
casePath = r'D:\python_daima\learning-genie\testcase'
discover = unittest.defaultTestLoader.discover(start_dir=casePath)
reportPath = r'D:\\python_daima\\learning-genie\\report'+'result.html'
fp = open(reportPath,'wb')
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title='Learning-genie Report',description='主要用于 LG 登录模块的测试报告',retry=1)
runner.run(discover)
fp.close()