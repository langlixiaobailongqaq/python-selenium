# coding:utf-8
from selenium import webdriver
import time

"""
  获取当前窗口句柄
    1.元素有属性，浏览器的窗口其实也有属性的，只是你看不到，浏览器窗口的属性用句柄（handle）来识别。
    2.人为操作的话，可以通过眼睛看，识别不同的窗口点击切换。但是脚本没长眼睛，它不知道你要操作哪个窗口，这时候只能句柄来判断了。
    3.获取当前页面的句柄：driver.current_window_handle
"""
driver = webdriver.Chrome()
driver.get("http://bj.ganji.com")
driver.implicitly_wait(5)
# 获取当前窗口句柄
h = driver.current_window_handle
# print(h)


"""
三、获取所有句柄
    1.定位赶集网招聘求职按钮，并点击
    2.点击后，获取当前所有的句柄：window_handles
"""
print(h)  # 打印首页句柄
driver.find_element_by_link_text("高薪工作").click()
all_h = driver.window_handles
print(all_h) # 打印所有的句柄


"""
四、切换句柄
网上大部分教程都是些的第一种方法，这里新增一个更简单的方法，直接从获取所有的句柄list里面取值。
方法一（不推荐）：
    1.循环判断是否与首页句柄相等
    2.如果不等，说明是新页面的句柄
    3.获取的新页面句柄后，可以切换到新打开的页面上
    4.打印新页面的title,看是否切换成功
方法二：
    1.直接获取all_h这个list数据里面第二个hand的值：all_h[1]
"""

"""
# 方法一：判断句柄，不等于首页就切换
for i in all_h :
    if i != h :
        driver.switch_to_window(i)
        print(driver.title)
"""
# 方法二：获取list里面第二个直接切换
driver.switch_to_window(all_h[1])
print(driver.title)


"""
五、关闭新窗口，切回主页
   1.close是关闭当前窗口，因为此时有两个窗口，用close可以关闭其中一个，quit是退出整个进程（如果当前有两个窗口，会一起关闭）。
   2.切换到首页句柄：h
   3.打印当前页面的title，看是否切换到首页了
"""
# 关闭新窗口
driver.close()
# 切换到首页句柄
driver.switch_to_window(h)
# 打印当前的title
print(driver.title)