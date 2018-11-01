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
        """测试模块管理列表展示"""

        response = self.client.get("/manage/module_manage/")
        #获取返回的页面内容
        res_html = response.content.decode("utf-8")
        # print("res_html",response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn("test0001",res_html)
        self.assertIn("退出", res_html)
        self.assertIn("单测模块名称", res_html)

    def test_module_add(self):
        """测试模块管理新增"""

        p_id = Project.objects.get(pname="项目名称1").id
        # response = self.client.get("/manage/module_add/")
        # print("content=", response.content.decode("utf-8"))
        response=self.client.post("/manage/module_add/", {"project": p_id,"mname":"添加模块1","description": "添加模块描述1"})
        # print("CONTENT",response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/manage/module_manage/")
        # 获取返回的页面内容
        res_html = response.content.decode("utf-8")
        self.assertIn("test0001",res_html)
        self.assertIn("退出", res_html)
        #断言新增的数据是否在页面列表上
        self.assertIn("添加模块1", res_html)
        #查询数据数据是否已添加,查询返回记录数
        p_res=Module.objects.filter(mname="添加模块1")
        self.assertEqual(p_res.count(),1)
        #验证数据库数据
        self.assertEqual(p_res[0].mname, "添加模块1")
        self.assertEqual(p_res[0].description, "添加模块描述1")



    def test_module_edit(self):
        """测试项目管理修改"""
        # 获取新增项目的id
        p_id = Project.objects.get(pname="项目名称1").id
        # 获取新增数据的id，用于修改数据传参
        mid = Module.objects.get(mname="单测模块名称").id
        # 注意点：module_edit/mid 后面没有"/" ！！！！！！
        response = self.client.post("/manage/module_edit/"+str(mid),
                                    {"project": p_id, "mname": "单测模块名称修改", "description": "单测模块名称描述修改"})
        print("CONTENT",response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/manage/module_manage/")
        # 获取返回的页面内容
        res_html = response.content.decode("utf-8")
        self.assertIn("test0001",res_html)
        self.assertIn("退出", res_html)
        #断言修改的数据是否在页面列表上
        self.assertIn("单测模块名称修改", res_html)
        #查询数据数据是否已修改,查询返回记录数
        m_res=Module.objects.filter(id=mid)
        self.assertEqual(m_res.count(), 1)
        #验证数据库数据是否已修改
        self.assertEqual(m_res[0].mname, "单测模块名称修改")
        self.assertEqual(m_res[0].description, "单测模块名称描述修改")



    def test_module_delete(self):
        """测试项目管理删除"""

        # 获取新增数据的id，用于修改数据传参
        mid = Module.objects.get(mname="单测模块名称").id
        response = self.client.get("/manage/module_delete/"+str(mid))
        # print("CONTENT",response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/manage/module_manage/")
        # 获取返回的页面内容
        res_html = response.content.decode("utf-8")
        self.assertIn("test0001",res_html)
        self.assertIn("退出", res_html)
        #断言删除的数据是否已不在页面列表上
        self.assertNotIn("单测模块名称", res_html)
        self.assertNotIn("单测模块名称描述", res_html)
        #查询数据数据是否已删除,查询返回记录数应为0
        m_res=Module.objects.filter(id=mid)
        self.assertEqual(m_res.count(),0)


