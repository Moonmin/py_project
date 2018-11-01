from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

class IndexPageTest(TestCase):
    """登录页面测试"""

    def test_get_index_page_template(self):
        """登录页面返回模板名称测试"""

        response = self.client.get("/") #client:Django 的测试客户端,这个类，就像一个虚拟的Web浏览器
        self.assertEqual(response.status_code,200)#判断响应码
        self.assertTemplateUsed(response,"login.html")

class LoginActionTest(TestCase):
    """登录方法测试"""

    def setUp(self):
        #测试准备数据,创建用户，用于登录
        User.objects.create_user("test0001", "test001@163.com", "123")

    def test_login_uname_pwd_null(self):
        """用户名和密码为空"""

        response = self.client.post("/login_action/",{"user_name":"","password":""})
        #print(response.content.decode("utf-8"))
        login_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code,200)
        self.assertIn("用户名或密码为空",login_html)


    def test_login_uname_pwd_error(self):
        """用户名和密码错误"""

        response = self.client.post("/login_action/",{"user_name":"ali","password":"123"})
        # print(response.content.decode("utf-8"))
        login_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code,200)
        self.assertIn("用户名或密码错误",login_html)



    def test_login_succes(self):
        """登录成功"""

        response = self.client.post(
            "/login_action/",data={"user_name": "test0001", "password": "123"})
        print(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 302)


class LogoutTest(TestCase):
    """退出用例,初始化数据登录系统，再调用退出接口"""
    def setUp(self):
        #测试准备数据,创建用户,登录系统
        User.objects.create_user("test0001", "test001@163.com", "123")
        login_data = {"user_name": "test0001", "password": "123"}
        response = self.client.post(
            "/login_action/", data= login_data)
        # self.assertEqual(response.status_code,302)


    def test_logout(self):
        response = self.client.get("/logout/")
        # print("cotent=",response.content.decode("utf-8"))
        self.assertEqual(response.status_code,302)
