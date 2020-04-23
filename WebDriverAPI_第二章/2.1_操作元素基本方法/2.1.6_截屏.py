# coding:utf-8
from selenium import webdriver
import time


# 1. 打开网站之后，也可以对屏幕截屏
# 2.截屏后设置指定的保存路径+文件名称+后缀
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)
driver.get_screenshot_as_file("D:\\Pycharm\\Pycharm\\python-selenium\\b1.jpg")


