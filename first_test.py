from Commonlib.Commonlib import Commonshare
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # 实例化Common
        self.com_obj = Commonshare()

    def tearDown(self):
        # 退出浏览器
        self.com_obj.__del__()

    def test_001(self):
        # # 访问百度VMware Tools
        # self.com_obj.open_url("http://www.baidu.com")
        # # 输入内容
        # self.com_obj.input_data("id", "kw", "selenium")
        # # 点击搜索
        # self.com_obj.click("id", "su")
        self.assertEqual("1", "1")

    def test_002(self):
        self.assertEqual("1", "2")

if __name__ == '__main__':
    # unittest.main()
    # 创建测试套件
    suit = unittest.TestSuite()
    # 向测试套件添加测试用例
    case_list = ["test_001", "test_002"]
    for case in case_list:
        suit.addTest(Test(case))
    # 运行测试套件
    unittest.TextTestRunner(verbosity=2).run(suit)
