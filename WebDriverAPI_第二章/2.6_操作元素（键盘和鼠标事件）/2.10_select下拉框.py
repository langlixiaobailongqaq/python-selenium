# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains # 鼠标事件
from selenium.webdriver.support.ui import Select

"""
一、认识select
    1.打开百度-设置-搜索设置界面，
    
    二、二次定位
    1.定位select里的选项有多种方式，这里先介绍一种简单的方法：二次定位
    2.基本思路，先定位select框，再定位select里的选项            
    3.代码如下：
"""
driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)
driver.implicitly_wait(10)
# 鼠标移动到"设置"按钮
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()


# 分两步：先定位下拉框并点击它，再点击选项
driver.find_element_by_name("NR").click()
driver.find_element_by_xpath("//option[@value ='50']").click()


"""
select_by_index()  :通过索引定位
select_by_value()  :通过value值定位
select_by_visible_text() :通过文本值定位
deselect_all()          ：取消所有选项
deselect_by_index()     ：取消对应index选项
deselect_by_value()      ：取消对应value选项
deselect_by_visible_text() ：取消对应文本选项

first_selected_option()  ：返回第一个选项
all_selected_options()   ：返回所有的选项

"""



