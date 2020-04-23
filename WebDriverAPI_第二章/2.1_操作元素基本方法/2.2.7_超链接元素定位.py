# coding:utf-8
from selenium import webdriver


"""
1.从元素属性可以分析出，有个href = "http://www.hao123.com
说明它是个超链接，对于这种元素，可以用以下方法：
"""
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_link_text("hao123").click()


