from django.contrib import admin
from django.urls import path,re_path,include
from project_app import views

urlpatterns = [
    path("project_manage/",views.project_manage),
    path("add_project/", views.add_project),
    re_path(r"^manage_edit/(\d+)/$", views.edit_project),
    re_path(r"^manage_delete/(\d+)/$", views.delete_project)

]