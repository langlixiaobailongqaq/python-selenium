# coding: utf-8
from selenium import webdriver
# 导入time模块
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# 设置休眠时间3秒，也可以是小数，单位秒
time.sleep(3)
# 等待3秒后刷新页面
driver.refresh()
