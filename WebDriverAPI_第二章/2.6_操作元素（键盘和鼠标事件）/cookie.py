from selenium import webdriver
import pprint,time
import json
import requests
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
"""


driver = webdriver.Chrome()
"""
driver.get("https://www.cnblogs.com/")
time.sleep(3)

# 登录
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("input1").send_keys("xxx")
driver.find_element_by_id("input2").send_keys("xxx")
driver.find_element_by_id("signin").click()
driver.implicitly_wait(30)

# 获取cookie并通过json模块将dict转化成str
dictCookies = driver.get_cookies()
jsonCookies = json.dumps(dictCookies)
print(jsonCookies)
# 登录完成后，将cookie保存到本地文件
with open('cookies.json', 'w') as f:
    f.write(jsonCookies)
"""


# 初次建立连接，随后方可修改cookie
driver.get("https://www.cnblogs.com/xiao-bai-long/")
# 删除第一次建立连接时的cookie
driver.delete_all_cookies()
# 读取登录时存储到本地的cookie
with open('cookies.json', 'r', encoding='utf-8') as f:
    listCookies = json.loads(f.read())
   # print(listCookies)

"""
for cookie in listCookies:
    driver.add_cookie({
        'domain': '.passport.cnblogs.com',  # 此处xxx.com前，需要带点
        'name': cookie['name'],
        'value': cookie['value'],
        'path': '/',
        'expires': None
    })
    print(listCookies)
"""

driver.add_cookie({
        'domain': '.cnblogs.com',  # 此处xxx.com前，需要带点
        'name': 'AspxAutoDetectCookieSupport',
        'value': '1',
        'path': '/',
        'expires': None
    })
# 再次访问页面，便可实现免登陆访问
driver.get('https://home.cnblogs.com/u/xiao-bai-long/')



"""
url = 'https://www.cnblogs.com/'
headers = {
    'cookie': cookiestr,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

html = requests.get(url=url, headers=headers)
print(html.text)
driver.get('https://home.cnblogs.com/u/xiao-bai-long/')
"""
