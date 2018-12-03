from django.contrib import admin
from django.urls import path,re_path,include
from interface_app.views import case_views,task_views,case_api

urlpatterns = [
    # 用例管理
    path("case_manage/",case_views.case_manage),
    path("case_save/", case_views.save_case),
    path("get_project_list/", case_views.get_project_list),#查询项目模块列表
    path("search_name/", case_views.get_search_case_list),  # 查询项目模块列表带查询条件
    path("/get_case_info/", case_api.get_case_info),  # 获取修改数据
    path("add_case/", case_views.add_case),  # 创建页面
    path("edit_case/<int:cid>", case_views.edit_case),  # 编辑/调试用例
    path("del_case/<int:cid>", case_views.del_case),  # 删除用例


    path("debug_interface/", case_views.debug_interface),  # 发送调试接口请求

    # re_path(r"^manage_edit/(\d+)/$", project_views.edit_project),
    # re_path(r"^manage_delete/(\d+)/$", project_views.delete_project),
    # 任务管理
    path("task_manage/", task_views.task_manage),
    # path("module_add/", module_views.add_module),
    # path("module_edit/<int:mid>", module_views.edit_module),
    # path("module_delete/<int:mid>", module_views.delete_module),

]