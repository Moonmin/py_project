from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep
from django.contrib.auth.models import User
from project_app.models import Project


class LoginTest(StaticLiveServerTestCase):
    """登录功能ui测试"""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()


    def setUp(self):
        """初始化数据"""
        User.objects.create_user("test0001", "test01@mail.com", "123")
        Project.objects.create(pname="测试平台项目", description="描述")

    def test_login_uname_isnull(self):
        """用户名密码为空"""

        self.driver.get("%s%s" %(self.live_server_url, "/"))
        user_name_input = self.driver.find_element_by_name("user_name")
        user_name_input.send_keys("")
        pwd_input = self.driver.find_element_by_name("password")
        pwd_input.send_keys("")
        sleep(1)
        self.driver.find_element_by_id("login_btn").click()
        error_hint = self.driver.find_element_by_id("err_hint").text
        print(error_hint)
        self.assertEqual("用户名或密码为空", error_hint)


    def test_login_error(self):
        """用户名密码为空"""

        self.driver.get("%s%s" %(self.live_server_url, "/"))
        user_name_input = self.driver.find_element_by_name("user_name")
        user_name_input.send_keys("22222")
        pwd_input = self.driver.find_element_by_name("password")
        pwd_input.send_keys("22222")
        sleep(1)
        self.driver.find_element_by_id("login_btn").click()
        error_hint = self.driver.find_element_by_id("err_hint").text
        print(error_hint)
        self.assertEqual("用户名或密码错误", error_hint)



    def test_login_success(self):
        """用户名密码正确"""

        self.driver.get("%s%s" % (self.live_server_url, "/"))
        user_name_input = self.driver.find_element_by_name("user_name")
        user_name_input.send_keys("test0001")
        pwd_input = self.driver.find_element_by_name("password")
        pwd_input.send_keys("123")
        sleep(1)
        self.driver.find_element_by_id("login_btn").click()
        sleep(1)
        #获取页面左上角平台名称
        page_name_text = self.driver.find_element_by_class_name("navbar-brand").text
        # print(page_name_text)
        self.assertEqual("测试平台", page_name_text)
        #登录用户
        login_name_text = self.driver.find_element_by_id("login_name")






        def add_project():
            """新增页面ui"""

            self.driver.find_element_by_id("add_btn").click()
            add_project_page_name = self.driver.find_element_by_id("add_project_page").text
            # print("add_project_page_name=",add_project_page_name)
            self.assertEqual("添加项目", add_project_page_name)
            p_name_text = self.driver.find_element_by_id("id_pname")
            p_name_text.send_keys("ui项目名称")
            id_description_text = self.driver.find_element_by_id("id_description")
            id_description_text.send_keys("ui描述")
            self.driver.find_element_by_id("btn_save").click()
            # 获取列表数据断言
            p_name = self.driver.find_element_by_xpath("//tr[1]/td[1]").text
            p_description = self.driver.find_element_by_xpath("//tr[1]/td[2]").text
            # print("p_description=",p_description)
            self.assertEqual("ui项目名称", p_name)
            self.assertEqual("p_description", p_description)

            
