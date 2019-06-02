from selenium import webdriver
import time

class Commonshare:
    def __init__(self):
        # 创建浏览器
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(3)
        # 浏览器全屏
        self.driver.maximize_window()

    def open_url(self, url):
        # 打开浏览器
        self.driver.get(url)
        # 隐式等待
        self.driver.implicitly_wait(5)

    # 对定位元素的封装
    def locateElement(self, locate_type, value):
        """
        :param locate_type: 元素类型
        :param value: 元素的值
        :return: 定位的元素
        """
        el = None
        if locate_type == "id":
            el = self.driver.find_element_by_id(value)
        elif locate_type == "name":
            el = self.driver.find_element_by_name(value)
        elif locate_type == "class":
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == "text":
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == "partial":
            el = self.driver.find_element_by_partial_link_text(value)
        elif locate_type =="tag":
            el = self.driver.find_element_by_tag_name(value)
        elif locate_type == "xpath":
            el = self.driver.find_element_by_xpath(value)
        elif locate_type == "css":
            el = self.driver.find_element_by_css_selector(value)
        # 返回定位的元素
        if el is not None:
            return el

    # 对点击元素的封装
    def click(self, locate_type, value):
        # 调用locateElement
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        el.click()

    # 对定位到的元素进行文本输入
    def input_data(self, locate_type, value, data):
        # 调用locateElement
        el = self.locateElement(locate_type, value)
        # 执行输入数据操作
        el.send_keys(data)

    # 获取定位到的元素的文本内容，如：<element>text</element>
    def get_text(self, locate_type, value):
        # 调用locateElement
        el = self.locateElement(locate_type, value)
        # 获取元素文本内容
        return el.text

    # 获取定位到的元素的标签属性
    def get_attr(self, locate_type, value, data):
        # 调用locateElement
        el = self.locateElement(locate_type, value)
        # 获取元素属性
        return el.get_attribute(data)

    def close_url(self):
        # 关闭浏览器窗口，一次只关闭一个
        self.driver.close()

    def __del__(self):
        time.sleep(3)
        # 退出浏览器窗口，关闭全部浏览器
        self.driver.quit()

if __name__ == '__main__':
    com = Commonshare()
    com.open_url("http://www.baidu.com")
    com.input_data("id", "kw", "selenium")
    com.click("id", "su")
    time.sleep(5)
    com.driver.close()
