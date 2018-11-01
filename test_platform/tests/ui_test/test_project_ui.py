from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep
from django.contrib.auth.models import User
from project_app.models import Project


class ProjectManageTest(StaticLiveServerTestCase):
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
        """初始化数据，登录系统"""
        User.objects.create_user("test0001", "aaa@mail.com", "123")
        Project.objects.create(pname="ui测试平台项目", description="ui项目描述")
        self.driver.get("%s%s" % (self.live_server_url, "/"))
        user_name_input = self.driver.find_element_by_name("user_name")
        user_name_input.send_keys("test0001")
        pwd_input = self.driver.find_element_by_name("password")
        pwd_input.send_keys("123")
        self.driver.find_element_by_id("login_btn").click()





    def test_project_list(self):
        """项目列表"""
        # 获取页面左上角平台名称，确认已登录系统
        page_name_text = self.driver.find_element_by_class_name("navbar-brand").text
        print(page_name_text)
        self.assertEqual("测试平台", page_name_text)
        # 获取列表数据断言
        p_name = self.driver.find_element_by_xpath("//tr[1]/td[1]").text
        p_description = self.driver.find_element_by_xpath("//tr[1]/td[2]").text
        # print("p_description=",p_description)
        self.assertEqual("ui测试平台项目", p_name)
        self.assertEqual("ui项目描述", p_description)


    def test_add_project(self):
        """新增页面ui"""
        # 获取页面左上角平台名称，确认已登录系统
        page_name_text = self.driver.find_element_by_class_name("navbar-brand").text
        print(page_name_text)
        self.assertEqual("测试平台", page_name_text)
        self.driver.find_element_by_id("add_btn").click() # 项目新增
        add_project_page_name = self.driver.find_element_by_id("add_project_page").text
        self.assertEqual("添加项目", add_project_page_name) # 确认打开新增页面
        p_name_text = self.driver.find_element_by_id("id_pname")
        p_name_text.send_keys("ui项目名称2")
        id_description_text = self.driver.find_element_by_id("id_description")
        id_description_text.send_keys("ui项目描述2")
        self.driver.find_element_by_id("btn_save").click()
        # 获取列表数据断言
        p_name = self.driver.find_element_by_xpath("//tr[2]/td[1]").text
        p_description = self.driver.find_element_by_xpath("//tr[2]/td[2]").text
        # print("p_description=",p_description)
        self.assertEqual("ui项目名称2", p_name)
        self.assertEqual("ui项目描述2", p_description)


    def test_edit_project(self):
        """新增页面ui"""
        # 获取页面左上角平台名称，确认已登录系统
        page_name_text = self.driver.find_element_by_class_name("navbar-brand").text
        print(page_name_text)
        self.assertEqual("测试平台", page_name_text)
        pid = Project.objects.get(pname="ui测试平台项目").id # 获到projectid用于编辑操作的id
        # print("pid=",pid)
        self.driver.find_element_by_id("op_edit"+ str(pid)).click() # 项目修改
        add_project_page_name = self.driver.find_element_by_id("edit_project_page").text
        self.assertEqual("修改项目", add_project_page_name) # 确认打开修改页面
        p_name_text = self.driver.find_element_by_id("id_pname")
        p_name_text.clear()
        p_name_text.send_keys("ui项目名称2修改")
        id_description_text = self.driver.find_element_by_id("id_description")
        id_description_text.clear()
        id_description_text.send_keys("ui项目描述2修改")
        self.driver.find_element_by_id("btn_save").click()
        # 获取列表数据断言
        p_name = self.driver.find_element_by_xpath("//tr[1]/td[1]").text
        p_description = self.driver.find_element_by_xpath("//tr[1]/td[2]").text
        # print("p_description=",p_description)
        self.assertEqual("ui项目名称2修改", p_name)
        self.assertEqual("ui项目描述2修改", p_description)


    def test_edit_project(self):
        """修改页面ui"""
        # 获取页面左上角平台名称，确认已登录系统
        page_name_text = self.driver.find_element_by_class_name("navbar-brand").text
        print(page_name_text)
        self.assertEqual("测试平台", page_name_text)
        pid = Project.objects.get(pname="ui测试平台项目").id # 获到projectid用于编辑操作的id
        # print("pid=",pid)
        self.driver.find_element_by_id("op_edit"+ str(pid)).click() # 项目修改
        add_project_page_name = self.driver.find_element_by_id("edit_project_page").text
        self.assertEqual("修改项目", add_project_page_name) # 确认打开修改页面
        p_name_text = self.driver.find_element_by_id("id_pname")
        p_name_text.clear()
        p_name_text.send_keys("ui项目名称2修改")
        id_description_text = self.driver.find_element_by_id("id_description")
        id_description_text.clear()
        id_description_text.send_keys("ui项目描述2修改")
        self.driver.find_element_by_id("btn_save").click()
        # 获取列表数据断言
        p_name = self.driver.find_element_by_xpath("//tr[1]/td[1]").text
        p_description = self.driver.find_element_by_xpath("//tr[1]/td[2]").text
        # print("p_description=",p_description)
        self.assertEqual("ui项目名称2修改", p_name)
        self.assertEqual("ui项目描述2修改", p_description)


    def test_del_project(self):
        """删除功能ui"""
        # 获取页面左上角平台名称，确认已登录系统
        page_name_text = self.driver.find_element_by_class_name("navbar-brand").text
        print(page_name_text)
        self.assertEqual("测试平台", page_name_text)
        pid = Project.objects.get(pname="ui测试平台项目").id# 获到projectid用于编辑操作的id
        # print("pid=",pid)
        self.driver.find_element_by_id("op_del" + str(pid)).click()# 项目删除
        # 获取列表数据断言
        tbody_list = self.driver.find_element_by_xpath("//tbody").text
        print("tbody_list",str(tbody_list))
        self.assertEqual("", tbody_list) #列表信息为空
