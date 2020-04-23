# coding:utf-8
from selenium import webdriver
import time

"""
alert\confirm\prompt弹出框操作主要方法有：
text：获取文本值
accept() ：点击"确认"
dismiss() ：点击"取消"或者叉掉对话框
send_keys() ：输入文本值 --仅限于prompt,在alert和confirm上没有输入框
"""

"""
二、alert操作

   1.先用switch_to_alert()方法切换到alert弹出框上
    2.可以用text方法获取弹出的文本 信息
    3.accept()点击确认按钮
    4.dismiss()相当于点右上角x，取消弹出框
   （url的路径，直接复制浏览器打开的路径）
"""
driver = webdriver.Chrome()
url = "file:///C:/Users/Admin/Desktop/selenium练习网页/Alert.html"
driver.get(url)
time.sleep(3)


driver.find_element_by_id("alert").click()
time.sleep(4)
t = driver.switch_to_alert()
# 打印警告框文本内容
print(t.text)
# 点击警告确认按钮
t.accept()

# 点击X按钮，取消
# t.dismiss()



"""
三、confirm操作
   1.先用switch_to_alert()方法切换到alert弹出框上
    2.可以用text方法获取弹出的文本 信息
    3.accept()点击确认按钮
    4.dismiss()相当于点取消按钮或点右上角x，取消弹出框
（url的路径，直接复制浏览器打开的路径）
"""

driver.find_element_by_id("confirm").click()
time.sleep(3)
t = driver.switch_to_alert()
# 打印警告框文本内容
print(t.text)
# 点警告框确认按钮
t.accept()

# 点击取消
# t.dismiss()


"""
四、prompt操作
"""
driver.find_element_by_id("prompt").click()
time.sleep(3)
t = driver.switch_to_alert()
# 打印警告文本框内容
print(t.text)
t.send_keys("hello selenium")
# 点击警告框确认按钮
t.accept()
# 取消
# t.dismiss()
driver.close()