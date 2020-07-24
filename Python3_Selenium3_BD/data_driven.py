"""
5.2、数据驱动之参数化驱动和txt文件数据驱动

"""
# coding:utf-8
from selenium import webdriver
import time

search_text = ['python', '中文', 'text']
for keys in search_text:
	driver = webdriver.Chrome()
	# 隐式等待
	driver.implicitly_wait(10)
	driver.get("https://www.baidu.com/")
	driver.find_element_by_id('kw').send_keys(keys)
	time.sleep(3)
	driver.find_element_by_id('su').click()
	time.sleep(2)
	driver.quit()

