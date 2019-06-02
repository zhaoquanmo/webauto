from selenium import webdriver
import time

# 创建浏览器
driver = webdriver.Chrome()

# 访问163.com
url = "https://mail.163.com/"
driver.get(url)
time.sleep(5)

# 定位iframe
el = '#{}'.format(driver.find_element_by_css_selector("#loginDiv > iframe").get_attribute("id"))
# print(el)
# el_id = '"#' + el + '"'
# print(el_id)
# 切换表单
driver.switch_to.frame(el)

# 输入账号
driver.find_element_by_name("email").send_keys("zhaoquan_mo")
# 输入密码
driver.find_element_by_name("password").send_keys("q#*897717915")
# 点击登录
driver.find_element_by_id("dologin").click()

# 关闭窗口
driver.quit()

