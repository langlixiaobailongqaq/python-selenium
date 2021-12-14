from selenium.webdriver.support.relative_locator import locate_with
from selenium import webdriver
"""
selenium 4.0-新相对定位方式
        toLeftOf()：位于指定元素左侧的元素。 toRightOf()：位于指定元素右侧的元素。
        above()：相对于指定元素位于上方的元素。 below()：相对于指定元素位于下方的元素。 
        near()：元素距离指定元素最多50个像素。像素值可以修改。
"""


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.implicitly_wait(5)
shezhi = driver.find_element(By.ID, "su")
# above() 用于要查找的元素在指定元素的上方。
search_input = driver.find_element(locate_with(By.TAG_NAME,  "span").above(shezhi))
search_input.click()
