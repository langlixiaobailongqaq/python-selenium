# coding:utf-8
from selenium import webdriver


"""
1.xptah 可以通过元素的id、name、class定位,也可以通过标签,层级定位
2.xpath是一种路径语言，跟上面的定位原理不太一样，首先第一步要先学会用工具/或用Chrome浏览器查看一个元素的xpath。
        用Chrome浏览器查看一个元素的xpath：  1.找到元素的位置;2.悬停在查找到的位置，然后鼠标右键菜单中选择【copy】->【Copy XPath】        
"""
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 用xpath通过id属性定位
driver.find_element_by_xpath("//*[@id='kw']").send_keys("Python")
# 用xpath通过name属性定位
driver.find_element_by_xpath("//*[@name='wd']").send_keys("Python")
# 用xpath通过class属性定位
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("Python")
# 用xpath其它属性定位
driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys("Python")


# xpath:层级
# 通过定位它老爸老定位input输入框
driver.find_element_by_xpath("//span[@id='s_kw_wrap']/input").send_keys("Python")
# 通过定位它爷爷定位input输入框
driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("Python")


# xpath:索引-用xpath定位老大、老二和老三（这里索引是从1开始算起的，跟Python的索引不一样）
# 通过xpath定位老大
driver.find_element_by_xpath("//select[@id='nr']/option[1]").click()
# 通过xpath定位老二
driver.find_element_by_xpath("//select[@id='nr']/option[2]").click()
# 通过xpath定位老三
driver.find_element_by_xpath("//select[@id='nr']/option[3]").click()


# 2.3.6 xpath:逻辑运算-xpath还有一个比较强的功能，是可以多个属性逻辑运算的，可以支持与（and）、或（or）、非（not）
driver.find_element_by_xpath("//*[@id='kw' and @autocomplete='off']").click()



# 2.3.7 xpath:模糊匹配
# xpath模糊匹配功能
driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()
# xpath也可以模糊匹配某个属性
driver.find_element_by_xpath("//*[contains(@id,'kw')]").click()
# xpath也可以模糊匹配以什么开头
driver.find_element_by_xpath("//*[starts-with(@id,'s_kw_')]").click()
# xpath可以模糊匹配以什么结尾
driver.find_element_by_xpath("//*[ends-with(@id,'kw_wrap')]").click()
# # xpath支持正则表达式
driver.find_element_by_xpath("//*[matchs(text(),'hao13')]").click()


