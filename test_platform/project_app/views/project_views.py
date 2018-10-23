from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from project_app.models import Project
from project_app.forms import ProjectForm

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
    return render(request, "project_manage.html", {"cuser_name": cuser_name,
                                                 "latest_project_list": latest_project_list,
                                                "type": "list"}
                  )



def add_project(request):
    """
    新增项目
    :param request:
    :return:
    """
    if request.method == 'POST':
        # print("POSTPOSTPOST")
        #创建表单实例并使用请求中的数据填充它,绑定数据至表单
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
        # print("add_form",add_form.as_p())
        return render(request, "project_manage.html", {"add_form": add_form, "type": "add"})


def edit_project(request, nid):
    """
    修改项目
    :param request:
    :param nid:
    :return:
    """

    if request.method == "GET":#打开编辑页面
        #print("id=",nid)
        project_list = Project.objects.filter(id=nid)
        # print("project_rs",project_list[0].pname)
        #返回编辑页面
        # edit_form = ProjectForm(instance=project_list)
        # edit_form = ProjectForm(initial={"pname": project_list[0].pname,"description": project_list[0].description,"status": project_list[0].status })
        # print("edit_form",edit_form)
        edit_form = ProjectForm(
                instance=Project.objects.get(id=nid))
        return render(request, 'project_manage.html', {'edit_form': edit_form, "type": "edit", "id":project_list[0].id})

    else:
        # post请求,提交修改内容
        # 创建表单实例并使用请求中的数据填充它,绑定数据至表单
        form = ProjectForm(request.POST)
        # print("editeditediteditedit")
        # 检查表单内容是否有效
        if form.is_valid():
            # 读取表单返回的值
            e_pname = form.cleaned_data["pname"]
            e_description = form.cleaned_data["description"]
            e_status = form.cleaned_data["status"]
            # print("pname=",pname, "description=",description, "status=",status)
            Project.objects.filter(id=nid).update(pname=e_pname, description=e_description, status=e_status)
            # Project.save()
            return HttpResponseRedirect("/manage/project_manage/")
        else:
            return ""

def delete_project(request,nid):
    """
    删除项目
    :param request:
    :param nid:
    :return:
    """
    if request.method == "GET":
        Project.objects.get(id=nid).delete()
        return HttpResponseRedirect("/manage/project_manage/")
