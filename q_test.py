from selenium import webdriver
import time

# 创建一个浏览器对象
driver = webdriver.Chrome()
# # 设置全屏
# driver.maximize_window()
# # 获取当前浏览器尺寸
# size = driver.get_window_size()
# # 设置浏览器尺寸
# size1 = driver.set_window_size(400, 400)
# 获取浏览器位置
position = driver.get_window_position()
# 设置浏览器位置
position1 = driver.set_window_position(100, 0)

# # 传入一个地址
# url = "https://www.baidu.com"
# driver.get(url)
# e1 = driver.find_element_by_id("kw")
# e1.send_keys("selenium")

# driver.quit()
time.sleep(10)
driver.close()
