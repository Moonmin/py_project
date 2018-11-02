from django.contrib import admin
from django.urls import path,re_path,include
from interface_app.views import case_views,task_views

urlpatterns = [
    # 用例管理
    path("case_manage/",case_views.case_manage),
    # path("add_project/", project_views.add_project),
    # re_path(r"^manage_edit/(\d+)/$", project_views.edit_project),
    # re_path(r"^manage_delete/(\d+)/$", project_views.delete_project),
    # 任务管理
    path("task_manage/", task_views.task_manage),
    # path("module_add/", module_views.add_module),
    # path("module_edit/<int:mid>", module_views.edit_module),
    # path("module_delete/<int:mid>", module_views.delete_module),
    # 调试页面
    path("api_debug/", case_views.api_debug),
]