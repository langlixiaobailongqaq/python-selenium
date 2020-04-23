# coding:utf-8
from selenium import webdriver
import time

"""
单选框和复选框（radiobox、checkbox）

三、单选：radio
  1.首先是定位选择框的位置
"""
driver = webdriver.Chrome()
url = "file:///C:/Users/Admin/Desktop/selenium练习网页/checkbox.html"
driver.get(url)
driver.find_element_by_id("boy").click()
time.sleep(3)
driver.find_element_by_id("girl").click()
time.sleep(2)

"""四、复选框：checkbox"""
# driver.find_element_by_id("c1").click()
# time.sleep(2)

""" 五、全部勾选："""
# 复数，只能先获取到所有的checkbox对象，然后通过for循环去一个个点击操作
"""
checkboxs = driver.find_elements_by_xpath("//input[@type='checkbox']")
for i in checkboxs:
    i.click()
time.sleep(2)
"""

""" 六、判断是否选中：is_selected()"""
# 没操作前，判断选项框状态
s = driver.find_element_by_id("c1").is_selected()
print(s)
driver.find_element_by_id("c1").click()
# 点击后，判断元素是否为选中状态
r = driver.find_element_by_id("c1").is_selected()
print(r)
# 复选框单选
driver.find_element_by_id("c1").click()
checkboxs = driver.find_elements_by_xpath("//input[@type='checkbox']")
for i in  checkboxs:
    i.click()
