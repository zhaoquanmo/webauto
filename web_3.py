from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)

e1 = driver.find_element_by_id("kw")
print(e1.size)
print(e1.is_displayed())


driver.quit()