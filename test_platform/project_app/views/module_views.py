from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from project_app.models import Module
from project_app.forms import ModuleForm

# Create your views here
@login_required
def list_module(request):
    # 单测时发现切换到模块管理页面时，右上角登录用户丢失，加上从session中获取用户
    cuser_name = request.session.get("cuser_name", "")
    latest_module_list = Module.objects.all()
    #增加返回标签type,用于区分操作
    return render(request, "module_manage.html", {"cuser_name": cuser_name,"latest_module_list": latest_module_list,
                                                "type": "list"}
                  )

@login_required
def add_module(request):
    """
    新增模块
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        #检查表单内容是否有效
        if form.is_valid():
            #读取表单返回的值
            project_id = form.cleaned_data["project"]
            print("project_id=====",project_id,type(project_id))
            mname = form.cleaned_data["mname"]
            description = form.cleaned_data["description"]
            Module.objects.create(project=project_id,mname=mname, description=description)
            return HttpResponseRedirect("/manage/module_manage/")

    else:
        #新增页面,返回forms中定义的表单
        add_form = ModuleForm()
        # print("add_form",add_form.as_p())
        return render(request, "module_manage.html", {"add_form": add_form, "type": "add"})

@login_required
def edit_module(request, mid):
    """
    修改模块
    :param request:
    :param mid:
    :return:
    """

    if request.method == "GET":#打开编辑页面
        edit_form = ModuleForm(
                instance=Module.objects.get(id=mid))
        return render(request, 'module_manage.html', {'edit_form': edit_form, "type": "edit"})

    else:
        form = ModuleForm(request.POST)
        # 检查表单内容是否有效
        if form.is_valid():
            # 读取表单返回的值
            e_project = form.cleaned_data["project"]
            e_mname = form.cleaned_data["mname"]
            e_description = form.cleaned_data["description"]
            Module.objects.filter(id=mid).update(project=e_project,mname=e_mname, description=e_description)
            # Project.save()
            return HttpResponseRedirect("/manage/module_manage/")
        else:
            return ""

@login_required
def delete_module(request,mid):
    """
    删除模块
    :param request:
    :param nid:
    :return:
    """
    if request.method == "GET":
        Module.objects.get(id=mid).delete()
        return HttpResponseRedirect("/manage/module_manage/")
