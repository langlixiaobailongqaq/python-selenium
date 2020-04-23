# coding:utf-8
from selenium import webdriver


"""
1.有时候一个超链接它的字符串可能比较长，如果输入全称的话，会显示很长，这时候可以用一模糊匹配方式，
        截取其中一部分字符串就可以了
2.如“hao123”,只需输入“ao123”也可以定位到
"""
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_partial_link_text("ao123").click()


