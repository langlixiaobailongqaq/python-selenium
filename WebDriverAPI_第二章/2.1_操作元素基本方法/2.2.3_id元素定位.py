# coding:utf-8
from selenium import webdriver


"""
1.从百度定位到的元素属性中，可以看到有个id属性：id="kw"，这里可以通过它的id属性定位到这个元素。
2.定位到搜索框后，用send_keys()方法，输入文本。
"""
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Python")


