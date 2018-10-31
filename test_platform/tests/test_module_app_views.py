from django.test import TestCase
from project_app.models import Project,Module
from django.test import Client
from django.contrib.auth.models import User




# Create your tests here.

class ModuleViewsTest(TestCase):
    """模块管理视图测试
       测试用例：
       1.新增列表展示接口
       2.新增接口
       3.修改接口
       4.删除接口

    """
    def setUp(self):
        #测试准备数据,创建用户，用于登录
        User.objects.create_user("test0001", "test001@163.com", "123")
        self.client = Client()
        login_data = {"user_name": "test0001", "password": "123"}
        self.client.post('/login_action/', data=login_data)
        #创建项目、模块数据用于测试
        project = Project.objects.create(pname="项目名称1", description="项目名称描述1")
        Module.objects.create(project=project, mname="单测模块名称", description="单测模块名称描述")


    def test_module_manage(self):
        """测试项目管理列表展示"""

        response = self.client.get("/manage/project_manage/")
        #获取返回的页面内容
        res_html = response.content.decode("utf-8")
        # print("res_html",response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn("test0001",res_html)
        self.assertIn("退出", res_html)
        self.assertIn("项目名称1", res_html)

    def test_project_add(self):
        """测试项目管理新增"""

        # self.client.get("/manage/add_project/")
        response = self.client.post("/manage/add_project/", {"pname":"添加项目","description": "添加项目描述"})
        # print("CONTENT",response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/manage/project_manage/")
        # 获取返回的页面内容
        res_html = response.content.decode("utf-8")
        self.assertIn("test0001",res_html)
        self.assertIn("退出", res_html)
        #断言新增的数据是否在页面列表上
        self.assertIn("添加项目", res_html)
        #查询数据数据是否已添加,查询返回记录数
        p_res=Project.objects.filter(pname="添加项目")
        self.assertEqual(p_res.count(),1)
        #验证数据库数据
        self.assertEqual(p_res[0].pname, "添加项目")
        self.assertEqual(p_res[0].description, "添加项目描述")
        self.assertEqual(p_res[0].status,0)


    def test_project_edit(self):
        """测试项目管理修改"""

        # 获取新增数据的id，用于修改数据传参
        pid = Project.objects.get(pname="项目名称1").id
        # print("pid",pid)
        response = self.client.post("/manage/manage_edit/"+str(pid)+"/", {"pname":"添加项目修改","description": "添加项目描述修改","status": 1})
        # print("CONTENT",response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/manage/project_manage/")
        # 获取返回的页面内容
        res_html = response.content.decode("utf-8")
        self.assertIn("test0001",res_html)
        self.assertIn("退出", res_html)
        #断言修改的数据是否在页面列表上
        self.assertIn("添加项目修改", res_html)
        #查询数据数据是否已修改,查询返回记录数
        p_res=Project.objects.filter(id=pid)
        self.assertEqual(p_res.count(),1)
        #验证数据库数据是否已修改
        self.assertEqual(p_res[0].pname, "添加项目修改")
        self.assertEqual(p_res[0].description, "添加项目描述修改")
        self.assertEqual(p_res[0].status, 1)


    def test_project_delete(self):
        """测试项目管理删除"""

        # 获取新增数据的id，用于修改数据传参
        pid = Project.objects.get(pname="项目名称1").id
        # print("pid",pid)
        response = self.client.get("/manage/manage_delete/"+str(pid)+"/")
        # print("CONTENT",response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/manage/project_manage/")
        # 获取返回的页面内容
        res_html = response.content.decode("utf-8")
        self.assertIn("test0001",res_html)
        self.assertIn("退出", res_html)
        #断言删除的数据是否已不在页面列表上
        self.assertNotIn("项目名称1", res_html)
        self.assertNotIn("添加项目描述1", res_html)
        #查询数据数据是否已删除,查询返回记录数应为0
        p_res=Project.objects.filter(id=pid)
        self.assertEqual(p_res.count(),0)


