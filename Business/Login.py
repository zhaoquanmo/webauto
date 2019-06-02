from Commonlib.Commonlib import Commonshare

class Login(Commonshare):
    def login(self, user, pwd):
        # 打开浏览器
        self.open_url("")
        # 定位登陆页面
        self.click("id", "")
        # 输入账号
        self.input_data("id", "", user)
        # 输入密码
        self.input_data("id", "", pwd)
        # 点击登陆
        self.click("id", "")

if __name__ == '__main__':
    login = Login()
    login.login("", "")
