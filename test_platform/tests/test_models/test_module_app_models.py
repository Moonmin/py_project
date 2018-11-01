from django.test import TestCase
from project_app.models import Module
from project_app.models import Project

# Create your tests here.

class ModuleModelsTest(TestCase):
    """模块模型测试"""

    @classmethod
    def setUpTestData(cls):
        """
        测试准备数据，新增项目管理数据，在每个测试函数之前被调用
        setUpTestData()，用于类级别设置，在测试运行开始的时侯，会调用一次。
        可以使用它来创建在任何测试方法中，都不会修改或更改的对象
        :return:
        """
        Project.objects.create(pname="单测项目名称", description="单测项目名称描述")
        p_res = Project.objects.get(pname="单测项目名称")
        Module.objects.create(project=p_res,mname="单测模块名称", description="单测模块名称描述")
        m_res = Module.objects.get(mname="单测模块名称")

    def test_mname_label(self):
        """测试模块模型mname字段标签名称"""
        module = Module.objects.get(id=1)
        field_label = module._meta.get_field("mname").verbose_name
        # print("field_name=",field_label)
        self.assertEqual(field_label,"名称")

    def test_description_label(self):
        """测试模块模型description字段标签名称"""
        module = Module.objects.get(id=1)
        field_label = module._meta.get_field("description").verbose_name
        self.assertEqual(field_label,"描述")

    def test_mname_max_length(self):
        """测试mname的最大长度"""
        module = Module.objects.get(id=1)
        max_length = module._meta.get_field("mname").max_length
        self.assertEqual(max_length,255)

    def test_description_max_length(self):
        """测试description的最大长度"""
        module = Module.objects.get(id=1)
        max_length = module._meta.get_field("description").max_length
        self.assertEqual(max_length,255)

    def test_module_add(self):
        """模块表新增测试"""

        p_res = Project.objects.get(pname="单测项目名称")#获取模块关联项目信息
        module = Module.objects.create(project=p_res,mname="模块名称",description="模块名称描述")
        m_res = Module.objects.get(mname="模块名称")
        self.assertEqual(m_res.mname,"模块名称")
        self.assertEqual(m_res.description,"模块名称描述")


    def test_module_edit(self):
        """项目表修改测试"""

        Module.objects.filter(mname="单测模块名称").update(description="单测模块描述修改")
        m_res = Module.objects.get(mname="单测模块名称")
        self.assertEqual(m_res.mname,"单测模块名称")
        self.assertEqual(m_res.description,"单测模块描述修改")


    def test_module_delete(self):
        """模块表删除测试"""

        Module.objects.get(mname="单测模块名称").delete()
        m_res_count = Module.objects.filter(mname="单测模块名称").count()
        self.assertEqual(m_res_count, 0)
