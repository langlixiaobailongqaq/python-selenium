# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标事件

"""
    1.鼠标不仅仅可以点击(click),鼠标还有其它的操作，如：鼠标悬停在某个元素上，鼠标右击，鼠标按住某个按钮拖到
    2.鼠标事件需要先导入模块：from selenium.webdriver.common.action_chainsimport ActionChains
        perform() 执行所有ActionChains中的行为；
        move_to_element() 鼠标悬停。
    3.这里以百度页面设置按钮为例：
     4.除了常用的鼠标悬停事件外，还有
       右击鼠标：context_click()
       双击鼠标：double_click()
"""
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(5)
# 鼠标悬停在搜索设置按钮上
mouse =driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
