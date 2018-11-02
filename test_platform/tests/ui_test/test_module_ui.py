from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep
from django.contrib.auth.models import User
from project_app.models import Project,Module


class ModuleManageTest(StaticLiveServerTestCase):
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
        p_res = Project.objects.create(pname="ui测试平台项目", description="ui项目描述")
        Module.objects.create(project=p_res, mname="ui模块名称", description="ui模块名称描述")
        self.driver.get("%s%s" % (self.live_server_url, "/"))
        user_name_input = self.driver.find_element_by_name("user_name")
        user_name_input.send_keys("test0001")
        pwd_input = self.driver.find_element_by_name("password")
        pwd_input.send_keys("123")
        self.driver.find_element_by_id("login_btn").click()
        # 打开模块管理页面
        self.driver.find_element_by_link_text("模块管理").click()




    def test_module_list(self):
        """模块列表"""

        # 模块名称
        p_name = self.driver.find_element_by_xpath("//tr[1]/td[2]").text
        # 描述
        p_description = self.driver.find_element_by_xpath("//tr[1]/td[3]").text
        # print("p_description=",p_description)
        self.assertEqual("ui模块名称", p_name)
        self.assertEqual("ui模块名称描述", p_description)


    def test_add_module(self):
        """新增页面ui"""

        self.driver.find_element_by_id("add_btn").click() # 模块新增
        add_project_page_name = self.driver.find_element_by_id("add_module_page").text
        self.assertEqual("添加模块", add_project_page_name) # 确认打开新增页面
        self.driver.find_element_by_xpath("//select/option[2]").click()
        p_name_text = self.driver.find_element_by_id("id_mname")
        p_name_text.send_keys("ui模型名称3")
        id_description_text = self.driver.find_element_by_id("id_description")
        id_description_text.send_keys("ui模块描述3")
        self.driver.find_element_by_id("btn_save").click()
        # 获取列表数据断言
        m_name = self.driver.find_element_by_xpath("//tr[2]/td[2]").text
        m_description = self.driver.find_element_by_xpath("//tr[2]/td[3]").text
        # print("p_description=",p_description)
        self.assertEqual("ui模型名称3", m_name)
        self.assertEqual("ui模块描述3", m_description)


    def test_edit_module(self):
        """修改页面ui"""

        mid = Module.objects.get(mname="ui模块名称").id # 获到projectid用于编辑操作的id
        # print("pid=",pid)
        self.driver.find_element_by_id("op_edit"+ str(mid)).click() # 项目修改
        edit_module_page_name = self.driver.find_element_by_id("edit_module_page").text
        self.assertEqual("修改模块", edit_module_page_name) # 确认打开修改页面
        m_name_text = self.driver.find_element_by_id("id_mname")
        m_name_text.clear()
        m_name_text.send_keys("ui模块名称修改")
        id_description_text = self.driver.find_element_by_id("id_description")
        id_description_text.clear()
        id_description_text.send_keys("ui模块描述修改")
        self.driver.find_element_by_id("btn_save").click()
        # 获取列表数据断言
        m_name = self.driver.find_element_by_xpath("//tr[1]/td[2]").text
        m_description = self.driver.find_element_by_xpath("//tr[1]/td[3]").text
        # print("p_description=",p_description)
        self.assertEqual("ui模块名称修改", m_name)
        self.assertEqual("ui模块描述修改", m_description)





    def test_del_project(self):
        """删除功能ui"""
        # 获取页面左上角平台名称，确认已登录系统
        mid = Module.objects.get(mname="ui模块名称").id  # 获到projectid用于编辑操作的id
        # print("pid=",pid)
        self.driver.find_element_by_id("op_del" + str(mid)).click()# 项目删除
        # 获取列表数据断言
        tbody_list = self.driver.find_element_by_xpath("//tbody").text
        print("tbody_list",str(tbody_list))
        self.assertEqual("", tbody_list) #列表信息为空
