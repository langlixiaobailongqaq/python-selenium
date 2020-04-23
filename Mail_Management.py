# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://106.75.171.52:9003/login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_xpath("//*[@class='btn btn-login btn-block']").click()
time.sleep(3)

driver.find_element_by_class_name("nav-label").click()
time.sleep(3)
driver.find_element_by_xpath("//li[14]/a[@class='J_menuItem']").click()
time.sleep(3)

# 用iframe上的div找到iframe
iframe = driver.find_element_by_xpath("//div[@id='content-main']/iframe[2]")
driver.switch_to.frame(iframe)

# 添加邮件按钮
driver.find_element_by_xpath("//div[@class='columns pull-left']/button").click()
time.sleep(4)


# 用iframe上的div找到iframe
iframe1 = driver.find_element_by_id("layui-layer-iframe1")
print(1)
driver.switch_to.frame(iframe1)
print(2)



# 标题
driver.find_element_by_xpath("//input[@id='MailTitil']").click()
print("标题")
driver.find_element_by_id("MailTitil").send_keys("测试1")
print("标题1")

# 消息类型
driver.find_element_by_name("mailType").click()
driver.find_element_by_xpath("//option[@value ='1']").click()
# 用户id
driver.find_element_by_id("Receiver").send_keys("557792")
# 内容
driver.find_element_by_id("MailContent").send_keys("测试1")

# 奖励
driver.find_element_by_name("mailRewardType").click()
driver.find_element_by_xpath("//option[@value ='1']").click()  # 奖励类型
# 奖励数量
driver.find_element_by_xpath("//div[@class='col-sm-2']/input[@name='mailRewardValue']").click()
driver.find_element_by_xpath("//div[@class='col-sm-2']/input[@name='mailRewardValue']").send_keys(1)
time.sleep(1)

# 时间
driver.find_element_by_id("MailSendTime").click()
# driver.find_element_by_class_name("layui-laydate-footer")
print(3)
driver.find_element_by_xpath("//div[@class='laydate-footer-btns']/span[2]").click()
print(4)
# 发送
driver.find_element_by_xpath("//div[@class='col-sm-4 col-sm-offset-3']/a[@class='btn btn-primary']").click()

# 释放iframe.重新回到主页面上
driver.switch_to.default_content()