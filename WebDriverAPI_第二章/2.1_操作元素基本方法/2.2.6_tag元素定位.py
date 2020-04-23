# coding:utf-8
from selenium import webdriver


"""
1.从百度定位到的元素属性中，可以看到每个元素都有tag（标签）属性，如搜索框的标签属性，就是最前面的input。
2.很明显，在一个页面中，相同的标签有很多，所以一般不用标签来定位。以下例子，仅供参考和理解，运行肯定报错。
"""
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_tag_name("input").send_keys("Python")


