from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

class UserModelsTest(TestCase):
    """用户模型测试"""

    def setUp(self):
        #测试准备数据，在每个测试函数之前被调用
        User.objects.create_user("test0001","test001@163.com","123")

    def test_user_create(self):
        """创建用户"""
        User.objects.create_user("test0002","test002@163.com","123")
        # user = User.objects.get(username="test0001")
        # self.assertEqual(user.username,"test0001")
        user = User.objects.get(username="test0002")
        self.assertEqual(user.username,"test0002")
        self.assertEqual(user.email,"test002@163.com")

    def test_user_select(self):
        """查询用户"""
        user = User.objects.get(username="test0001")
        self.assertEqual(user.username,"test0001")
        self.assertEqual(user.email,"test001@163.com")


    def test_user_edit(self):
        """修改用户"""

        User.objects.filter(username="test0001").update(email="edit0001@163.com")
        user = User.objects.get(username="test0001")
        self.assertEqual(user.email,"edit0001@163.com")

    def test_user_delete(self):
        """删除用户"""
        User.objects.get(username="test0001").delete()
        #返回记录条数
        user_count = User.objects.filter(username="test0001").count()
        # print("user_name",user_count)
        self.assertEqual(user_count,0)