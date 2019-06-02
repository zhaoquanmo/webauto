from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
# 创建浏览器
driver = webdriver.Chrome()
# 全屏
driver.maximize_window()
# 访问百度
url = "http://www.baidu.com"
driver.get(url)
# 点击设置
el_link = driver.find_element_by_link_text("设置")
el_link.click()
# 选择搜索设置
el_search = driver.find_element_by_css_selector("#wrapper > div.bdpfmenu > a.setpref")
el_search.click()
time.sleep(3)
# 创建一个下拉对象
el_select = driver.find_element_by_id("nr")
el_obj = Select(el_select)
# 索引选择
# el_obj.select_by_index(0)
# time.sleep(2)
# el_obj.select_by_index(1)
# time.sleep(2)
# el_obj.select_by_index(2)
# time.sleep(2)
# # 值选择
# el_obj.select_by_value("10")
# time.sleep(2)
# el_obj.select_by_value("20")
# time.sleep(2)
# el_obj.select_by_value("50")
# time.sleep(2)
# # 文本选择
# el_obj.select_by_visible_text("每页显示50条")
# time.sleep(2)
# el_obj.select_by_visible_text("每页显示10条")
# time.sleep(2)
# el_obj.select_by_visible_text("每页显示20条")
# time.sleep(2)

# 点击保存设置
print(el_obj.first_selected_option.text)
for i in el_obj.all_selected_options:
    print("i:", i.text)
for e in el_obj.options:
    print("e", e.text)

el_save_set = driver.find_element_by_css_selector("#gxszButton > a.prefpanelgo")
el_save_set.click()
time.sleep(3)
# 接受
driver.switch_to.alert.accept()
# # 拒绝
# driver.switch_to.alert.dismiss()
# 退出浏览器
time.sleep(5)
driver.quit()