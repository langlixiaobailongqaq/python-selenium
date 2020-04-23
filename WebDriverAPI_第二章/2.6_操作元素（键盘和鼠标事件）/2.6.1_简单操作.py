# coding:utf-8
from selenium import webdriver


"""
 1.点击（鼠标左键）页面按钮：click()
    2.清空输入框：clear()
    3.输入字符串：send_keys()
    4.send_keys()如果是发送中文的，前面需加u，如：u"中文",因为这里是输入到windows系统了，windows系统是GBK编码，
        我们的脚本是utf-8,需要转码为Unicode国际编码，这样才能识别到。
"""

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# implicitly_wait是隐式等待，作用全局
driver.implicitly_wait(5)
driver.find_element_by_id("kw").clear()
# send_keys 里如果是中文的话，前面加u
driver.find_element_by_id("kw").send_keys(u"上海-悠悠")
driver.find_element_by_id("su").click()
