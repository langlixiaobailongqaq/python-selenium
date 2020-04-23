
# coding=utf-8
from selenium import webdriver
# 配置文件地址


# 用Chrome地址栏输入chrome://version/，查看自己的“个人资料路径”，然后在浏览器启动时，调用这个配置文件
# C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default

"""
# 加载Chrome配置
option = webdriver.ChromeOptions()
# option.add_argument(r'--user-agent = xx')
driver = webdriver.Chrome(chrome_options=option)
driver.implicitly_wait(30)
driver.get("http://www.cnblogs.com/yoyoketang/")
"""

option = webdriver.ChromeOptions()
# 伪装iphone登录
# option.add_argument(r'--user-agent = C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Defaul')
# 伪装android
option.add_argument(r'--user-agent = C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Defaul')
driver = webdriver.Chrome(chrome_options=option)
driver.get('http://www.taobao.com/')

