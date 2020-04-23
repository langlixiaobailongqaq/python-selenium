from selenium import webdriver

url = "file:///C:/Users/Admin/Desktop/selenium练习网页/table.html"
driver = webdriver.Chrome()
driver.get(url)
t = driver.find_element_by_xpath(".//*[@id='myTable']/tbody/tr[2]/td[1]")
print(t.text)