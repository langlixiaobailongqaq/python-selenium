# coding:utf-8
from selenium import webdriver


"""
1.从百度定位到的元素属性中，可以看到有个class属性：class="s_ipt"，这里可以通过它的class属性定位到这个元素。
"""
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_class_name("s_ipt").send_keys("Python")


