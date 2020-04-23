
from selenium import webdriver
import time

# 打开浏览器
driver = webdriver.Chrome()     # 谷歌


# 打开jenkins
driver.get("http://192.168.0.74:8080/")
driver.maximize_window()

# 用户名,密码
driver.find_element_by_id("j_username").send_keys("zhengxin")
driver.find_element_by_name("j_password").send_keys("&gqJy7eFJV1m&i")
driver.find_element_by_name("Submit").submit()
# driver.implicitly_wait(10)
time.sleep(10)


# driver.find_element_by_link_text("打安卓AB资源").click()
# driver.implicitly_wait(5)
# driver.find_element_by_link_text("立即构建").click()
# driver.implicitly_wait(5)
#
# driver.find_element_by_xpath("//*[@class='permalinks-list']/li/a").click()
# driver.implicitly_wait(5)
# driver.find_element_by_link_text("控制台输出").click()


driver.find_element_by_link_text("查看安卓AB")
print("构建成功！")