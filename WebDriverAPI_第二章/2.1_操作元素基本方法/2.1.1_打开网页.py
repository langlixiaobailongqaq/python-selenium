# 2.1.1打开网页

# coding:utf-8
# 导入webdriver模块
from selenium import webdriver
# 打开浏览器
driver = webdriver.Chrome() # 谷歌

# driver = webdriver.Ie() # IE
# driver = webdriver.Firefox() # 火狐
# 打开百度
driver.get("https://www.baidu.com")




# 教程：https://www.cnblogs.com/zidonghua/p/7430083.html