# coning:utf-8
from selenium import webdriver
import time

"""获取title"""
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
time.sleep(2)
title = driver.title
print(title)


"""二、获取元素的文本 """
text = driver.find_element_by_id("setf").text
print(text)

"""三、获取元素的标签
1.获取百度输入框的标签属性"""
tag = driver.find_element_by_id("kw").tag_name
print(tag)

"""四、获取元素的其它属性
1.获取其它属性方法:get_attribute("属性")，这里的参数可以是class、name等任意属性
2.如获取百度输入框的class属性"""
name = driver.find_element_by_id("kw").get_attribute("class")
print(name)

"""
五、获取输入框内的文本值
1、如果在百度输入框输入了内容，这里输入框的内容也是可以获取到的
"""
driver.find_element_by_id("kw").send_keys("yoyoketang")
value = driver.find_element_by_id("kw").get_attribute("value")
print(value)

"""
六、获取浏览器名称
1.获取浏览器名称很简单，用driver.name就能获取到
"""
print(driver.name)
driver.quit()