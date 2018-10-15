from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from .models import Project

# Create your views here

'''
从session里面读取用户信息  
重定向请求跳转至新页面
'''

@login_required
def project_manage(request):
    # cuser_name = request.COOKIES.get("cuser_name","")
    # print("cuser_name=",cuser_name)
    cuser_name = request.session.get("cuser_name","")
    latest_project_list = Project.objects.all()
    #print("latest_project_id=",latest_project_list.get(pname="项目1"))
    #context = {"latest_project_list":latest_project_list}

    return render(request,"project_manage.html",{"cuser_name":cuser_name,"latest_project_list":latest_project_list})



#新增项目
def add_project(request):
    if request.method == 'POST':
        #print("POSTPOSTPOST")
        #新增提交
        pname = request.POST.get("pname")
        description = request.POST.get("description")
        status = request.POST.get("status","False")
        #print("status=",status)
        Project.objects.create(pname=pname,description=description,status=status)
        #跳转回首页
        return HttpResponseRedirect("/manage/project_manage/")
    elif request.method == "GET":
        #跳转新增页面
        return render(request, "project_manage_add.html")

#修改项目
def edit_project(request,nid):
    if request.method == "GET":
        #print("id=",nid)
        latest_project_list = Project.objects.filter(id=nid)
        print("latest_project_list=", latest_project_list)
        return render(request,'project_manage_edit.html', {'latest_project_list': latest_project_list})
    return ""


#删除项目
def delete_project(request):
    return ""