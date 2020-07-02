# -*- coding:utf-8 -*
from selenium.webdriver.support.ui import WebDriverWait
class Base():
    '''
    对 selenium 原生的查找元素方法进行二次封装
    30s 内循环查找页面上有没有这个元素
    这样封装的好处：
    1、可以有效提高查找元素的效率，避免元素没加载完成而抛异常
    2、相当于 sleep 和 implicitly time 更节省时间
    3、大大的减少代码重复，使用例书写更加简洁
    '''
    def __init__(self,driver):
        self.driver = driver
    def findEle(self,locator):
        '''
        定位方法参数化，
        :param locator: locator 参数是定位方式，如（'id','kw'）,把两个参数合并成一个元组
        * 号是传值时两个分开传值
        :return:
        '''
        element = WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element(*locator))
        return element
    def click(self,locator):
        ele = self.findEle(locator)
        ele.click()
    def sendKeys(self,locator,text,is_clear_first=False):
        ele = self.findEle(locator)
        if is_clear_first:
            ele.clear()  #is_clear_first 为 True 的时候执行
        ele.send_keys(text)
    def clear(self,locator):
        ele = self.findEle(locator)
        ele.clear()
    def get_text(self,locator):
        ele = self.findEle(locator)
        ele = ele.text
        return  ele


