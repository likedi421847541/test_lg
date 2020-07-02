# -*- coding:utf-8 -*-
from LG.Base import Base
class Login():
    def __init__(self,driver):
        self.driver = driver
        self.lg = Base(self.driver)
    def login(self,email,pwd):
        self.driver.get("https://web.learning-genie.com/#/login")
        self.loc1 = ('id','userEmail')
        self.loc2 =('id','userPassword')
        self.loc3 =('xpath','//button[@btn-loading="logging"]')
        self.lg.sendKeys(self.loc1,email)
        self.lg.sendKeys(self.loc2,pwd)
        self.lg.click(self.loc3)
        # self.driver.find_element_by_id('userEmail').send_keys(email)
        # self.driver.find_element_by_id('userPassword').send_keys(pwd)
        # self.driver.find_element_by_xpath("""//button[@btn-loading="logging"]""").click()
    def qingkong(self):
        self.lg.clear(self.loc1)
        self.lg.clear(self.loc2)
        # self.driver.find_element_by_id('userEmail').clear()
        # self.driver.find_element_by_id('userPassword').clear()
    def get_home(self):
        try:
            home = self.driver.find_element_by_xpath('//span[@translate="home"]').text
            return home
        except:
            return ''
    def get_empty_email(self):
        """
        如果没有输入邮箱登录，会获取提示语做断言
        :return:
        """
        empty_email = self.driver.find_element_by_id("emailEmpty").text
        return empty_email

    def get_empty_pwd(self):
        """
        如果没有密码登录，获取提示语做断言
        :return:
        """
        empty_email = self.driver.find_element_by_id("userErrorPassword").text
        return empty_email
    def get_error_emailtype(self):
        """
        如果输入的邮箱格式有误，获取提示语做断言
        :return:
        """
        error_email = self.driver.find_element_by_id("emailType").text
        return error_email
    def get_error(self):
        """
        如果输入的邮箱或密码有误，获取提示语做断言
        :return:
        """
        error =self.driver.find_element_by_xpath('//span[2]').text
        return  error
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     a = Login(driver)
#     a.login()
#     driver.quit()
