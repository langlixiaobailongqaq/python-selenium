# coding:utf-8
from selenium import webdriver


"""
css可以通过元素的id、class、标签这三个常规属性直接定位到
"""
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# 通过id
driver.find_element_by_css_selector("#kw").send_keys("Python")
# 通过class属性
driver.find_element_by_css_selector(".s_ipt").send_keys("Python")


# 2.4.2 css:其它属性
# css通过name属性
driver.find_element_by_css_selector("[name='wd']").send_keys("Python")
# css通过autocomplete属性
driver.find_element_by_css_selector("[autocomplete='off']").send_keys("Python")
# css通过type属性
driver.find_element_by_css_selector("[type='text']").send_keys("Python")


# 2.4.3 css:标签
driver.find_element_by_css_selector("input:contains('kw')")
# css通过标签与class属性的组合定位
driver.find_element_by_css_selector("input.s_ipt").send_keys("Python")
# css通过标签与id属性的组合定位
driver.find_element_by_css_selector("input#kw").send_keys("Python")
# css通过标签与其它属性的组合定位
driver.find_element_by_css_selector("input[id='kw']").send_keys("Python")


# 2.4.4 css:层级关系
# css通过层级关系定位
driver.find_element_by_css_selector("form#form>span>input").send_keys("Python")
# css通过层级关系定位
driver.find_element_by_css_selector("form.fm>span>input").send_keys("python")


# 2.4.5 css:索引
# 选择第一个option
driver.find_element_by_css_selector("select#nr>option:nth-child(1)").click()
# 选择第二个option
driver.find_element_by_css_selector("select#nr>option:nth-child(2)").click()
# 选择第三个option
driver.find_element_by_css_selector("select#nr>option:nth-child(3)").click()


# 2.4.6 css:逻辑运算
driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys("Python")



