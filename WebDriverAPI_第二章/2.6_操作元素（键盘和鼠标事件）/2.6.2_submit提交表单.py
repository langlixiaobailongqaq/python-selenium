# coding:utf-8
from selenium import webdriver


"""
1.在前面百度搜索案例中，输入关键字后，可以直接按回车键搜索，也可以点搜索按钮搜索。
2.submit()一般用于模拟回车键
"""
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(5)
driver.find_element_by_id("kw").send_keys(u"测试部落")
# sbmit()模拟enter见提交表单
driver.find_element_by_id("kw").submit()