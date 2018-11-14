from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from interface_app.forms import TestCaseForm
from project_app.models import Module
from interface_app.models import TestCase
import requests
import json


# Create your views here.

def case_manage(request):
    """
    用例管理页面
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "case_manage.html", {"type": "list"})
    else:
        return Http404("页面不存在！")


def api_debug(request):
    """
    打开调试页面
    :param request:
    :return:
    """
    if request.method == "GET":
        add_form = TestCaseForm()
        # print("add_form=====",add_form)
        return render(request, "api_debug.html", {"type": "debug", "add_form": add_form})
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
        module_id = request.POST.get("module")
        req_name = request.POST.get("req_name")
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        params = request.POST.get("req_parameter")
        req_type = request.POST.get("req_type")  # 请求类型form-data/JSON
        req_headers = request.POST.get("req_header")

        # 以下参数为空时默认赋空值
        if (params == "" or module_id == "" or req_name == "" or
                url == "" or method == "" or req_type == ""):
            return HttpResponse("必填参数为空,请检查!")

        # 为空时,赋默认值
        if params == "":
            params = "{}"

        if req_headers == "":
            req_headers = "{}"

        # 根据module_id获取module对象
        module_obj = Module.objects.get(id=module_id)
        # print ("module===", type(module_obj))

        # 生成数据

        TestCase.objects.create(name=req_name, module=module_obj, url=url,
                                req_method=method, req_header=req_headers,
                                req_type=req_type,
                                req_parameter=params)
        return HttpResponse("保存成功")


    else:
        return Http404("请求错误！")
