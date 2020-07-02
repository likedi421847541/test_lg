# -*- coding:utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
r =EC.title_is('百度一下，你就知道')(driver)
r1 = EC.title_contains("百度一下")(driver)
r2 = EC.text_to_be_present_in_element('','wang')(driver)
print(r,r1)
assert r,r1
driver.quit()
class hello():
    def __call__(self, a):
        print (a)
if __name__ == '__main__':
    h = hello()
    h("hello")