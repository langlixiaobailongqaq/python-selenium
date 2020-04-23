# coding:utf-8
from selenium import webdriver
import re   # 正则表达式模块


"""
一、page_source
1.selenium的page_source方法可以直接返回页面源码
2.重新赋值后打印出来
"""
driver = webdriver.Chrome()
driver.get("http://www.cnblogs.com/yoyoketang/")
page = driver.page_source
# print(page)


"""
二、re非贪婪模式
1.这里需导入re模块(正则表达式模块)
2.用re的正则匹配：非贪婪模式
3.findall方法返回的是一个list集合
4.匹配出来之后发现有一些不是url链接，可以筛选下
"""
# 非贪婪匹配，re.s('.'匹配字符，包括换行符)
#url_list = re.findall('href=\"(.*?)\"', page, re.S)
#for url in url_list:
#    print(url)

"""
三、筛选url地址出来
1.加个if语句判断，‘http’在url里面说明是正常的url地址了
2.把所有的url地址放到一个集合，就是我们想要的结果啦
"""
url_list = re.findall('href=\"(.*?)\"', page, re.S)  # 注意是先单引号，再双引号
url_all = []
for url in url_list:
    if "http" in url:
        print(url)
        url_all.append(url)
# 最终的url集合
print(url_all)

# driver.quit()