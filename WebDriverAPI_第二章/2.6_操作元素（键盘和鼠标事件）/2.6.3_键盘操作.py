# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 键盘模块

"""
 1.selenium提供了一整套的模拟键盘操作事件，前面submit()方法如果不行的话，可以试试模拟键盘事件
    2.模拟键盘的操作需要先导入键盘模块：from selenium.webdriver.common.keysimport Keys
    3.模拟enter键，可以用send_keys(Keys.ENTER)
      4.其它常见的键盘操作：
       键盘F1到F12：send_keys(Keys.F1)把F1改成对应的快捷键：
       复制Ctrl+C：send_keys(Keys.CONTROL,'c') 
       粘贴Ctrl+V：send_keys(Keys.CONTROL,'v') 
       全选Ctrl+A：send_keys(Keys.CONTROL,'a') 
       剪切Ctrl+X：send_keys(Keys.CONTROL,'x') 
       制表键Tab:  send_keys(Keys.TAB) 
"""
driver = webdriver.Chrome()
driver.get("http://hordehome.com")
driver.implicitly_wait(5)
driver.find_element_by_id("search-button").click()
driver.find_element_by_id("search-term").clear()
driver.find_element_by_id("search-term").send_keys("selenium")
# 模拟enter键操作回车按钮
driver.find_element_by_id("search-term").send_keys(Keys.ENTER)
