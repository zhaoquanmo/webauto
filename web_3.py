from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "http://10.1.118.81:7001/ehome-admin/login.do"
driver.get(url)

el_user = driver.find_element_by_id("username")
el_user.send_keys("admin")

el_login = driver.find_element_by_css_selector("#myForm > div > input[type=button]")
el_login.click()

data = driver.switch_to.alert
print(data.text)
print(type(data))


time.sleep(10)
driver.quit()