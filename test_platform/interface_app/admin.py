from django.contrib import admin
from .models import TestCase

# Register your models here.


class TestCaseAdmin(admin.ModelAdmin):
    """
    定义管理页面的显示格式，显示以下字段
    """
    list_display = ["module", "name", "url", "req_method", "req_type",
                    "req_header", "req_param", "rsp_assert", "create_time", "creator"]



'''
向管理页面注册了 TestCase类,告诉管理页面，
TestCase 对象需要被管理
 '''
admin.site.register(TestCase, TestCaseAdmin)
