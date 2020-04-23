# coding:utf-8
from selenium import webdriver


"""
1.从百度定位到的元素属性中，可以看到有个name属性：name="wd"，这里可以通过它的name属性单位到这个元素。
    说明：这里运行后会报错，说明这个搜索框的name属性不是唯一的，无法通过name属性直接定位到输入框
"""
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_name("wd").send_keys("Python")


