# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


"""
  切换iframe
"""

bolgurl = "https://ueditor.baidu.com/website/onlinedemo.html"
driver = webdriver.Chrome()
driver.get(bolgurl)
driver.implicitly_wait(10)


iframe = driver.find_element_by_id("ueditor_0")
driver.switch_to.frame(iframe)
print(1)
driver.find_element_by_class_name('view').send_keys(Keys.TAB)
print(2)
driver.find_element_by_tag_name('body').send_keys("大萨达撒")
# 显示输入的值
print(driver.find_element_by_tag_name('body').text)
