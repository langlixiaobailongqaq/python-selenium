# coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from pymouse import PyMouse  # 专门模拟鼠标操作
from pykeyboard import PyKeyboard  # 专门模拟键盘上的操作
from login import *

m = PyMouse()
k = PyKeyboard()
"""
使用PyUserInput模块模拟鼠标键盘操作
一：SenKey :python3中没有该模块，PyUserInput模块安装前需要安装pywin32和pyHook模块,pywin32模块默认已安装
    1.需下载pyHook：https://www.lfd.uci.edu/~gohlke/pythonlibs/
            下载完成后，放在python/Scripts文件夹下，执行命令：pip install D:\Python3.5\Scripts\pyWinhook-1.6.1-cp35-cp35m-win_amd64.whl

    2.版本问题：选择下载自己python版本和系统版本相一致的pyHook版本。 如：本人是py35，64位，pyHook-1.5.1-cp35-cp35m-win_amd64.whl
                PyUserInput(0.1.11)版本不支持pyHook1.6版本，支持pyHook1.5版本

二：PyUserInput模块里面主要有两个类:
    1.PyMouse, 专门模拟鼠标操作
    2.PyKeyboard，专门模拟键盘上的操作
    
三.  问题：pywin32-221版本太高了，换成pywin32-220  
     pywin32-220下载地址：https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/
    先卸载pywin32: pip uninstall pywin32
"""


driver = webdriver.Chrome()
driver.get('https://www.cnblogs.com/')
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("input1").send_keys(data[0])
driver.find_element_by_id("input2").send_keys(data[1])
driver.find_element_by_id("signin").click()
driver.implicitly_wait(30)


driver.find_element_by_id("user_nav_blog_link").click()
driver.find_element_by_link_text("新随笔").click()

time.sleep(3)
# 点开编辑器图片
driver.find_element_by_css_selector("img.mceIcon").click()
time.sleep(3)
# 定位所有iframe,取第二个
iframe = driver.find_elements_by_tag_name('iframe')[1]
# 切换到iframe上
driver.switch_to.frame(iframe)
# 文件路径
time.sleep(2)
driver.find_element_by_class_name("qq-upload-button").click()
# driver.find_element_by_name("file").click()   ＃　这里点文件上传按钮也是一个坑，我用它父元素定位了，参考上面一行
time.sleep(5)
# 点击Shift键，切换英文输入法
k.tap_key(k.shift_key)
time.sleep(1)

# 键盘输入内容
k.type_string(r"D:\Pycharm\Pycharm\python-selenium\b1.jpg")  # 输入文件地址
time.sleep(1)
k.press_key(k.enter_key)  # 按住回车键
