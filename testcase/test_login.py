# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
import time
from LG.login import Login
class  test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.denglu = Login(cls.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.denglu.qingkong()
    def test_login(self):
        """
        测试登录的正常操作
        """
        self.denglu.login('test_123@q.cv','12345678q')
        self.assertTrue('首页',self.denglu.get_home())
    def test_login_EmptyEmail(self):
        """
        测试登录模块中空邮箱
        """
        self.denglu.login('','12345678q')
        self.assertTrue('手机号/邮箱不能为空！',self.denglu.get_empty_email())
    def test_login_EmptyPwd(self):
        """
        测试登录模块的空密码
        """
        self.denglu.login('mingchun@learninggenie.cn','')
        self.assertTrue('密码不能为空！',self.denglu.get_empty_pwd())
    def test_login_ErrorTypeEmail(self):
        """
        测试登录模块的邮箱格式有误
        """
        self.denglu.login('3123','12345678q')
        self.assertTrue('邮箱无效',self.denglu.get_error_emailtype())
    def test_error_pwd(self):
        """
        测试密码有误
        """
        self.denglu.login('3123@qq.com','12345')
        self.assertTrue('The username or password is incorrect.',self.denglu.get_error())
if __name__ == '__main__':
    unittest.main()