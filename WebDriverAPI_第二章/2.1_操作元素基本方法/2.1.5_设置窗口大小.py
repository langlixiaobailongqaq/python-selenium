# conding:utf-8

from selenium import webdriver
import time

# 可以设置浏览器窗口大小，如设置窗口大小为手机分辨率540*960
# 也可以最大化窗口
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)
# 设置窗口大小为540*960
driver.set_window_size(540, 960)
time.sleep(2)
# 将浏览器窗口最大化
driver.maximize_window()
