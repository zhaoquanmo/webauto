from selenium import webdriver
import time, os

# 创建一个浏览器
driver = webdriver.Chrome()
driver.maximize_window()

# 获取网页访问路径
file_path = "file:///" + os.path.abspath("example_frame.html")
# 访问路径文件
driver.get(file_path)
time.sleep(3)

# 切换表单1
driver.switch_to.frame("itcast_frame1")
# 切换表当2
driver.switch_to.frame("itcast_frame2")

# 输入内容
el_input = driver.find_element_by_id("sb_form_q")
el_input.send_keys("selenium")

# 点击搜索
el_submit = driver.find_element_by_id("sb_form_go")
el_submit.click()
print("在内层表单中")
try:
    el_id = driver.find_element_by_id("sb_form_q")
except:
    print("已退出表单")

# 关闭浏览器
# driver.quit()

