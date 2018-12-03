from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from interface_app.forms import TestCaseForm
from project_app.models import Module,Project
from interface_app.models import TestCase
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse,HttpResponseRedirect
import requests
import json


# Create your views here.

def get_project_list(request):
    """
    获取项目/模块列表
    :param request:
    :return:项目接口列表
    """
    if request.method == "GET":
        # 查询模块信息
        project_list = Project.objects.all()
        dataList = []# 定义list用于存放所有的项目名称-模块数据
        for project_data in project_list:#遍历模块表数据

            project_dict = \
                {
                    "name": project_data.pname #添加模块名称至数据字典中
                }
            # 根据模型查找对应模块数据
            # print("pid", project_data.id)
            module_list = Module.objects.filter(project_id=project_data.id)#不能用get！！！！！
            if len(module_list) != 0:
                module_name = []
                for module_data in module_list:
                    #module_dict = {module_data.id:module_data.mname}
                    #module_name.append(module_dict)
                    module_name.append(module_data.mname)

                project_dict["moduleList"] = module_name
                # print("每一行项目及模块",project_dict)
                dataList.append(project_dict)
        return JsonResponse({"success":"true", "data":dataList})
    else:
        return HttpResponse("请求无数据")


def get_search_case_list(request):
    """
    通过查询条件，获取项目/模块列表
    :param request:
    :return:项目接口列表
    """
    if request.method == "GET":
        case_name = request.GET.get("case_name")
        print("case_name=======",case_name)
        case_list = TestCase.objects.filter(name__contains=case_name)
        paginator = Paginator(case_list,5)#每页显示5条
        page = request.GET.get("page")#获取页面分页传的页数
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # 如果输入的页数不是整型，则取第一页
            contacts = paginator.page(1)
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页
            contacts = paginator.page(paginator.num_pages)

        return render(request, "case_manage.html", {"type": "list","case_list": contacts,"case_name": case_name})
    else:
        return Http404("页面不存在！")




def case_manage(request):
    """
    用例管理页面
    :param request:
    :return:
    """
    if request.method == "GET":
        case_list = TestCase.objects.all()
        paginator = Paginator(case_list,5)#每页显示5条

        page = request.GET.get("page")#获取页面分页传的页数
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # 如果输入的页数不是整型，则取第一页
            contacts = paginator.page(1)
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页
            contacts = paginator.page(paginator.num_pages)

        return render(request, "case_manage.html", {"type": "list","case_list": contacts})
    else:
        return Http404("页面不存在！")


def add_case(request):
    """
    打开调试页面
    :param request:
    :return:
    """
    if request.method == "GET":
        add_form = TestCaseForm()
        # print("add_form=====",add_form)
        return render(request, "case_add.html", {"type": "debug", "add_form": add_form})
    else:
        return Http404("请求错误！")


def debug_interface(request):
    """
    在线调试接口
    :param request:
    :return:
    """
    if request.method == "POST":
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        params = request.POST.get("req_parameter")
        payload = json.loads(params.replace("'", "\""))  # 参数字符串转json串
        req_type = request.POST.get("req_type")  # 请求类型form-data/JSON
        req_headers = request.POST.get("req_header")
        # print("headers====",req_headers)
        headers = json.loads(req_headers.replace("'", "\""))

        # 判断请求方法
        if method == "get":
            # payload = {'key1': 'value1', 'key2': 'value2'}# 参数形式为key:value形式
            r = requests.get(url, headers=headers, params=payload)

        elif method == "post":
            # 判断参数类型req_type：form-data /JSON
            # print("req_type===========",req_type)
            if req_type == "JSON":
                r = requests.post(url, headers=headers, data=json.dumps(payload))
            elif req_type == "form":
                r = requests.post(url, headers=headers, data=payload)
                print("r.url=== ", r.url, )

    return HttpResponse(r.text)


def save_case(request):
    """
    保存用例
    :param request:
    :return:
    """

    if request.method == "POST":
        # module_id = request.POST.get("module")
        module_name = request.POST.get("module")
        print("module_name",module_name)
        req_name = request.POST.get("req_name")
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        params = request.POST.get("req_parameter")
        req_type = request.POST.get("req_type")  # 请求类型form-data/JSON
        req_headers = request.POST.get("req_header")
        creator_id = request.POST.get("creator")
        print("creator_id==",creator_id)

        # 以下参数为空时默认赋空值
        if (params == "" or module_name == "" or req_name == "" or
                url == "" or method == "" or req_type == ""):
            return HttpResponse("必填参数为空,请检查!")

        # 为空时,赋默认值
        if params == "":
            params = "{}"

        if req_headers == "":
            req_headers = "{}"

        # 根据module_id获取module对象
        module_obj = Module.objects.get(mname=module_name)
        # print ("module===", type(module_obj))

        # 根据creator_id获取creator对象,用户写入时只需要写入id
        # creator_obj = User.objects.get(id=creator_id)
        # print ("creator_obj===", creator_obj)

        # 生成数据

        case_obj = TestCase.objects.create(name=req_name, module=module_obj, url=url,
                                req_method=method, req_header=req_headers,
                                req_type=req_type,
                                req_param=params,
                                creator_id=creator_id)
        if case_obj is not None:
            return HttpResponse("保存成功")
        else:
            return HttpResponse("保存失败")

    else:
        return Http404("请求错误！")


def edit_case(request,cid):
    """编辑用例"""
    if request.method == "GET":#打开编辑页面

        return render(request, 'case_edit.html', {"type": "edit"})

    else:#提交修改信息

        # 检查表单内容是否有效
        if form.is_valid():
            # 读取表单返回的值

            TestCase.objects.filter(id=cid).update()
            # Project.save()
            return HttpResponseRedirect("/interface/case_manage/")
        else:
            return ""


def del_case(request,cid):
    """
    删除用例
    :param request:
    :return:
    """
    if request.method == "GET":

        TestCase.objects.get(id=cid).delete()
        return HttpResponseRedirect("/interface/case_manage/")