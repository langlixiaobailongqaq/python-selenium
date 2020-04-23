# coding:utf-8
from selenium import webdriver
import time

"""
前提知识：
1、webdriver中提供了操作cookie的相关方法：
get_cookies()     　　              获得cookie信息
add_cookie(cookie_dict)         添加cookie
delete_cookie(name)              删除特定(部分)的cookie
delete_all_cookies()               删除所有的cookie
2、add_cookie()：其参数是一个字典，字典中必须有“name”和“value”两个key，可选的key是"path"、 "domin"、 "secure"、 "expiry"、"httponly"
key键的含义：
name：cookie的名称
value：cookie对应的值，动态生成的
domain：服务器域名
expiry：Cookie有效终止日期
path：Path属性定义了Web服务器上哪些路径下的页面可获取服务器设置的Cookie
httpOnly：防脚本攻击
secure:在Cookie中标记该变量，表明只有当浏览器和Web Server之间的通信协议为加密认证协议时

一、获取cookies：get_cookies()
1.获取cookies方法直接用：get_cookies()
2.先启动浏览器，获取cookies，打印出来发现是空：[]
3.打开博客首页后，重新获取cookies,打印出来，就有值了
"""

driver = webdriver.Chrome()
# # 启动浏览器后获取cookies
# print(driver.get_cookies())
# driver.get("https://www.cnblogs.com/xiao-bai-long/")
# time.sleep(3)
# # 打开主页后获取cookies
# print(driver.get_cookies())

"""
二、登录后的cookies
1.先登录博客园（这里登录用自己的账号和密码吧）
2.重新获取cookies，发现跟之前获取的不一样了
3.主要是找到这一个cookie,发现它的name和value发生了变化，这就是未登录和已登录的区别了（对比上下两张图）
{u'name': u'.CNBlogsCookie', u'value': u'B7813EBA142142CE88CC8C0B33B239F566xxxx'}
"""

# 登录后获取cookies
# url = "https://passport.cnblogs.com/user/signin"
# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(30)  # 隐式等待
# driver.find_element_by_id("LoginName").send_keys(u"浪里小白龙qaq")
# driver.find_element_by_id("Password").send_keys(u"Zx8331102@")
# driver.find_element_by_id("submitBtn").click()
# time.sleep(3)
# print(driver.get_cookies())

"""
三、获取指定name的cookie:driver.get_cookie（name）
1.获取cookies发现里面有多个cookie,有时候我们只需要其中的一个，把重要的提出来，比如登录的cookie
2.这里用get_cookie（name），指定对应的cookie的name值就行了，比如博客园的：.CNBlogsCookie
"""
# 登录后获取cookies
# url = "https://passport.cnblogs.com/user/signin"
# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(30)  # 隐式等待
# driver.find_element_by_id("LoginName").send_keys(u"浪里小白龙qaq")
# driver.find_element_by_id("Password").send_keys(u"Zx8331102@")
# driver.find_element_by_id("submitBtn").click()
# time.sleep(3)
# print(driver.get_cookies())
# 获取指定name的cookie
print(driver.get_cookie(name=".CNBlogsCookie"))


"""
四、清除指定cookie：delete_cookie()
1.为了进一步验证上一步获取到的就是登录的cookie，可以删除它看看页面什么变化
2.删除这个cookie后刷新页面，发现刚才的登录已经失效了，变成未登录状态了
"""
url = "https://passport.cnblogs.com/user/signin"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)  # 隐式等待
driver.find_element_by_id("LoginName").send_keys(u"浪里小白龙qaq")
driver.find_element_by_id("Password").send_keys(u"Zx8331102@")
driver.find_element_by_id("submitBtn").click()
time.sleep(4)
# 获取指定name的cookie
print(driver.get_cookie(name=".CNBlogsCookie"))

# 清除指定name的cookie
driver.delete_cookie(name=".CNBlogsCookie")
print(driver.get_cookies())
# 验证此cookie是可以登录，删除后刷新页面
driver.refresh()

"""
五、清除所有cookies：delete_all_cookies()
1.清除所有cookies后登录状态也失效了，cookies为空[]
"""
# 清除所有的cookie
driver.delete_all_cookies()
print(driver.get_cookies())