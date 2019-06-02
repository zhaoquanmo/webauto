from selenium import webdriver
import time

# 实例化driver
driver = webdriver.Chrome()

# 访问
url = "https://nj.58.com/chuzu/?PGTID=0d100000-000a-cd2b-c3bd-80b3698b2658&ClickID=2"
driver.get(url)

# 获取元素
# driver.find_element_by_name("tj_trnews").click()
# driver.find_element_by_class_name("a3").click()
# driver.find_element_by_link_text("习近平在红土地上这样谈“心”").click()
# driver.find_element_by_partial_link_text("习近平在红土地").click()
# driver.find_element_by_xpath('//*[@id="pane-news"]/div/ul/li[1]/strong/a').click()
# driver.find_element_by_css_selector('#pane-news > div > ul > li.hdline0 > strong > a').click()
# e1 = driver.find_elements_by_class_name('clearfix')
# print(e1.text)
# e = driver.find_element_by_id("kw")
# e.send_keys("selenium")
# e.clear()
# e.send_keys("java")
# print(e.get_attribute("id"))
# print(e.text)
# e2 = driver.find_element_by_id("su")
# print(e2.text)
# print(e2.get_attribute("value"))
# e2.submit()

e1_list = driver.find_elements_by_css_selector("body > div.list-wrap > div.list-box > ul > li:nth-child > div.des > h2 > a")
for i in e1_list:
    print("标题：", i.text, "链接：", i.get_attribute("href"))

time.sleep(5)
driver.close()
