# coding:utf-8
from selenium import webdriver
import time

"""
  一、frame和iframe区别
Frame与Iframe两者可以实现的功能基本相同，不过Iframe比Frame具有更多的灵活性。 frame是整个页面的框架，iframe是内嵌的网页元素，也可以说是内嵌的框架
Iframe标记又叫浮动帧标记，可以用它将一个HTML文档嵌入在一个HTML中显示。它和Frame标记的最大区别是在网页中嵌入 
的<Iframe></Iframe>所包含的内容与整个页面是一个整体，而<Frame>< /Frame>所包含的内容是一个独立的个体，是可以独立显示的。
另外，应用Iframe还可以在同一个页面中多次显示同一内容，而不必重复这段内 容的代码。

二、案例操作：163登录界面
1.打开http://mail.163.com/登录页面
2.用firebug定位登录框
3.鼠标停留在左下角（定位到iframe位置）时，右上角整个登录框显示灰色，说明iframe区域是整个登录框区域
4.左下角箭头位置显示iframe属性<iframe id="x-URS-iframe" frameborder="0" name="" 
"""

"""
 三、切换iframe
1.由于登录按钮是在iframe上，所以第一步需要把定位器切换到iframe上
2.用switch_to_frame方法切换，此处有id属性，可以直接用id定位切换
"""
driver = webdriver.Chrome()
driver.get("https://mail.163.com/")
driver.implicitly_wait(10)
# 切换iframe
# driver.switch_to_frame('x-URS-iframe1552532683421.2043') # ID是动态的数字，无法定位
# iframe = driver.find_element_by_xpath("//div[@id='loginDiv' and @class='loginUrs']/iframe")  # 用父标签找到iframe
# iframe = driver.find_element_by_tag_name("iframe")                          # tag标签类型找到iframe

# 用iframe上的第三个div找到iframe（在这里用父标签和tag无法定位到iframe,最后在爷爷标签上定位到）
iframe = driver.find_element_by_xpath("//div[@id='normalLoginTab']/div/div/iframe[@frameborder='0']")
driver.switch_to.frame(iframe)

driver.find_element_by_name("email").send_keys("123")
driver.find_element_by_name("password").send_keys("456")
# 释放iframe.重新回到主页面上
driver.switch_to.default_content()