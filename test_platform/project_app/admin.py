from django.contrib import admin
from .models import Project,Module

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    """
    定义管理页面的显示格式，显示以下字段
    """
    list_display = ["pname", "description", "status", "create_time", "id"]


class ModuleAdmin(admin.ModelAdmin):
    list_display = ["mname", "description", "create_time", "project_id", "id"]


admin.site.register(Project,ProjectAdmin)

'''
向管理页面注册了 Project类,告诉管理页面，
Project 对象需要被管理
 '''
admin.site.register(Module, ModuleAdmin)
