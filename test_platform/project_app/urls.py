from django.contrib import admin
from django.urls import path,re_path,include
from project_app.views import project_views,module_views

urlpatterns = [
    #项目管理
    path("project_manage/",project_views.project_manage),
    path("add_project/", project_views.add_project),
    re_path(r"^manage_edit/(\d+)/$", project_views.edit_project),
    re_path(r"^manage_delete/(\d+)/$", project_views.delete_project),
    #模型管理
    path("module_manage/", module_views.list_module),
    path("module_add/", module_views.add_module),
    path("module_edit/<int:mid>", module_views.edit_module),
    path("module_delete/<int:mid>", module_views.delete_module),

]