from Business.Login import Login
import unittest

class Test_login(unittest.TestCase):
    def setUp(self):
        print("start!")

    def tearDown(self):
        print("ending!")

    # 登录成功
    def test_001(self):
        log = Login()
        # 输入账号密码登录
        log.login("admin", "admin")
        # 获取用于断言判断的用户信息
        data = log.get_text("class", "col_yellow")
        # 进行断言判断
        self.assertEqual("所属机构：太平人寿   所属部门：工会管理室   姓名：系统用户", data)

    # 登录成功
    def test_002(self):
        log = Login()
        # 输入账号密码登录
        log.login("", "")
        # 获取用于断言判断的用户信息
        data = log.get_text("class", "col_yellow")
        # 进行断言判断
        self.assertEqual("所属机构：太平人寿   所属部门：工会管理室   姓名：系统用户", data)

if __name__ == '__main__':
    unittest.main()