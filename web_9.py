from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

# 创建浏览器
driver = webdriver.Chrome()
# 访问百度
url = "https://www.baidu.cn/"
driver.get(url)
# 显示等待
WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, 'lg')))
# 隐式等待
driver.implicitly_wait(10)
# 获取cookie
data = driver.get_cookies()
print(data)
# 删除cookie
driver.delete_all_cookies()
# 设置cookie
set_cookie = {"name": "H_PS_PSSID", "value": "1463_29164_21118_29063_28519_29098_28833_28584_26350_22157"}
data1 = driver.add_cookie(set_cookie)
print(data1)
