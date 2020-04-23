# coding:utf-8
from selenium import webdriver
import random  # 随机函数

"""
   1.在百度搜索框输入关键字“测试部落”后，用firebug查看页面元素，可以看到这些搜索结果有共同的属性。
   .从搜索的结果可以看到，他们的父元素一样：<h3 class="t">
    3.标签都一样，且target属性也一样：<a target="_blank" />
    4.于是这里可以用css定位（当然用xpath也是可以的）
"""
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.implicitly_wait(5)
driver.find_element_by_id("kw").send_keys(u"测试部落")
driver.find_element_by_id("kw").submit()
s = driver.find_elements_by_css_selector("h3.t > a")  # h3标签里的class=t,下的a标签
# 获取对象的属性，来验证下是不是定位准确了。这里可以获取href属性，打印出url地址。
for i in s:
    print (i.get_attribute('href'))



"""
三、随机函数
    1.搜索结果有10条，从这10条中随机取一个就ok了
    2.先导入随机函数：import random
    3.设置随机值范围为0~9：a=random.randint(0~9)
"""
# import random # 随机函数
# t = random.randint(0, 9)
# print(t)


"""
四、随机打开url
    1.从返回结果中随机取一个url地址
    2.通过get方法打卡url
    3.其实这种方式是接口测试了，不属于UI自动化，这里只是开阔下思维，不建议用这种方法
"""
# 设置随机值
# t = random.randint(0, 9)
# 随机取一个结果获取url地址
# a = s[t].get_attribute("href")
# print("******"+ a +"******")
# driver.get(a)

"""
五、通过click点击打开
    1.前面那种方法，是直接访问url地址，算是接口测试的范畴了，真正模拟用户点击行为，得用click的方法
"""
# 设置随机值
t= random.randint(0, 9)
# 随机取一个结果到点击鼠标
s[t].click()