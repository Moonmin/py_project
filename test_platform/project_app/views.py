from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from .models import Project
from .forms import ProjectForm

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
    #增加返回标签type,用于区分操作
    return render(request,"project_manage.html",{"cuser_name": cuser_name,
                                                 "latest_project_list": latest_project_list,
                                                "type": "list"}
                )



#新增项目
def add_project(request):
    if request.method == 'POST':
        print("POSTPOSTPOST")
        #创建表单实例并使用请求中的数据填充它
        form = ProjectForm(request.POST)
        #检查表单内容是否有效
        if form.is_valid():
            #读取表单返回的值
            pname = form.cleaned_data["pname"]
            description = form.cleaned_data["description"]
            status = form.cleaned_data["status"]
            Project.objects.create(pname=pname, description=description, status=status)
            return HttpResponseRedirect("/manage/project_manage/")

    elif request.method == "GET":
        #新增页面,返回forms中定义的表单
        add_form = ProjectForm()
        print("add_form",add_form.as_p())
        return render(request, "project_manage.html",{"add_form": add_form.as_p(),"type": "add"})

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