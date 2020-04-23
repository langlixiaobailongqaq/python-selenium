# coding:utf-8
from selenium import webdriver
import time



"""
1.退出有两种方式，一种是close;另外一种是quit。
2.close用于关闭当前窗口，当打开的窗口较多时，就可以用close关闭部分窗口。
3.quit用于结束进程，关闭所有的窗口。
4.最后结束测试，要用quit。quit可以回收c盘的临时文件。
"""
driver = webdriver.Chrome()
driver.get("https:www.baidu.com")
time.sleep(2)
# driver.close()
driver.quit()


