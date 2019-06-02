import unittest
from Commonlib.HTMLTestRunner import HTMLTestRunner
from Testcase.test_login import Test_login

class Test(unittest.TestCase):
    def test_suit(self):
        # 创建测试套件
        mysuit = unittest.TestSuite()
        # 向测试套件里添加测试用例
        case_list = ["test_001", "test_002"]
        for case in case_list:
            mysuit.addTest(Test_login(case))
        # # 运行测试套件
        # unittest.TextTestRunner(verbosity=2).run(mysuit)

        # 生成HTML测试报告步骤
        with open("../report.html", "wb") as f:
            HTMLTestRunner(
                stream=f,
                title="测试报告",
                description='测试报告描述。。。',
                verbosity=2
            ).run(mysuit)

if __name__ == '__main__':
    unittest.main()
