# coding:utf-8

from selenium import webdriver
import time
from login import *
"""

"""

driver = webdriver.Chrome()
driver.get('https://www.cnblogs.com/')
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("input1").send_keys(data[0])
driver.find_element_by_id("input2").send_keys(data[1])
driver.find_element_by_id("signin").click()
driver.implicitly_wait(30)

driver.find_element_by_id("user_nav_blog_link").click()
driver.find_element_by_link_text("新随笔").click()

time.sleep(3)
# 点开编辑器图片
driver.find_element_by_css_selector("img.mceIcon").click()
time.sleep(3)
# 定位所有iframe,取第二个
iframe = driver.find_elements_by_tag_name('iframe')[1]
# 切换到iframe上
driver.switch_to.frame(iframe)
# 文件路径
driver.find_element_by_name('file').send_keys(r"D:\Pycharm\Pycharm\python-selenium\b1.jpg")
