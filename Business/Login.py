from Commonlib.Commonlib import Commonshare

class Login(Commonshare):
    def login(self, user, pwd):
        # 打开浏览器
        self.open_url("http://10.1.118.81:7001/ehome-admin/login.do")
        # 输入账号
        self.input_data("id", "username", user)
        # 输入密码
        self.input_data("id", "password", pwd)
        # 点击登陆
        self.click("css", "#myForm > div > input[type=button]")

if __name__ == '__main__':
    login = Login()
    login.login("admin", "admin")
