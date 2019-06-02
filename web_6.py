from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# 创建一个浏览器
driver = webdriver.Chrome()
driver.maximize_window()
# 访问京东
url = "https://cn.bing.com/"
driver.get(url)
# # 定位元素
# el_list = driver.find_elements_by_id("cate_menu_item")
# # 移动鼠标
# for i in el_list:
#     ActionChains(driver).move_to_element(i).perform()
#     time.sleep(2)
#     print("执行成功：%s" % i)
# 定位元素
el = driver.find_element_by_id("sb_form_q")
# 输入内容
el.send_keys("selenium")
# 全选
el.send_keys(Keys.CONTROL, 'a')
time.sleep(2)
# 剪切
el.send_keys(Keys.CONTROL, 'x')
time.sleep(2)
# 粘贴
el.send_keys(Keys.CONTROL, 'v')
time.sleep(2)
# 清除
el.clear()
# 输入内容
el.send_keys("seleniumm")
# backspace一个
el.send_keys(Keys.BACKSPACE)
time.sleep(5)
# 点击回车键
el.send_keys(Keys.ENTER)
time.sleep(5)

# 退出
driver.quit()
