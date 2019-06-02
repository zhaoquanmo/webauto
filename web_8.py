from selenium import webdriver
import time

# 创建浏览器
driver = webdriver.Chrome()
# 访问hao123
url = "https://www.hao123.com/"
driver.get(url)
# 下拉滚动条
for i in range(100):
    # 方法一
    js = "window.scrollTo(0, %s)" % (i*100)
    driver.execute_script(js)
    time.sleep(0.1)
    # 方法二
    js1 = "var q=document.documentElement.scrollTop=%s" % (i*100)
    driver.execute_script(js1)
    time.sleep(0.2)
# 退出
# time.sleep(5)
driver.quit()
