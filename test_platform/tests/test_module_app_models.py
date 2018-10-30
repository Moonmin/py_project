from django.test import TestCase
from project_app.models import Module

# Create your tests here.

class ProjectModelsTest(TestCase):
    """模块模型测试"""

    @classmethod
    def setUpTestData(cls):
        """
        测试准备数据，新增项目管理数据，在每个测试函数之前被调用
        setUpTestData()，用于类级别设置，在测试运行开始的时侯，会调用一次。
        可以使用它来创建在任何测试方法中，都不会修改或更改的对象
        :return:
        """
        Module.objects.create(project="",mname="单测项目名称", description="单测项目名称描述")

    def test_pname_label(self):
        """测试项目模型mname字段标签名称"""
        module = Module.objects.get(id=1)
        field_label = module._meta.get_field("pname").verbose_name
        # print("field_name=",field_label)
        self.assertEqual(field_label,"名称")

    def test_description_label(self):
        """测试项目模型description字段标签名称"""
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field("description").verbose_name
        self.assertEqual(field_label,"描述")

    def test_pname_max_length(self):
        """测试pname的最大长度"""
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field("pname").max_length
        # print("max_length=",max_length)
        self.assertEqual(max_length,255)

    def test_description_max_length(self):
        """测试pname的最大长度"""
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field("description").max_length
        self.assertEqual(max_length,255)

    def test_project_add(self):
        """项目表新增测试"""
        project = Project.objects.create(pname="项目名称2",description="项目名称描述2")
        p_res = Project.objects.get(pname="项目名称2")
        self.assertEqual(p_res.pname,"项目名称2")
        self.assertEqual(p_res.description,"项目名称描述2")


    def test_project_edit(self):
        """项目表修改测试"""

        Project.objects.filter(pname="单测项目名称").update(description="单测项目描述修改")
        p_res = Project.objects.get(pname="单测项目名称")
        self.assertEqual(p_res.pname,"单测项目名称")
        self.assertEqual(p_res.description,"单测项目描述修改")


    def test_project_delete(self):
        """项目表删除测试"""

        Project.objects.get(pname="单测项目名称").delete()
        p_res_count = Project.objects.filter(pname="单测项目名称").count()
        self.assertEqual(p_res_count, 0)
