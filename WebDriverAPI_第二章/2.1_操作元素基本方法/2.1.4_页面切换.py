# cding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)
driver.get("http://www.hordehome.com")
time.sleep(3)
# 返回上一页
driver.back()
time.sleep(3)
# 切换到下一页
driver.forward()