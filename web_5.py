from selenium import webdriver
from selenium.webdriver import ActionChains

# 创建一个浏览器
driver = webdriver.Chrome()
# 访问百度
url = "http://www.baidu.com"
driver.get(url)

# 定位元素
el = driver.find_element_by_xpath('//*[@id="su"]')
# 鼠标右击操作
# ActionChains(driver).context_click(el).perform()
ActionChains(driver).double_click(el).perform()

# # 退出窗口
# driver.quit()