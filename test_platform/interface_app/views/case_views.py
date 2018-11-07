from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, JsonResponse
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
        return render(request, "case_manage.html",{"type":"list"})
    else:
        return Http404("页面不存在！")

def api_debug(request):
    """
    打开调试页面
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "api_debug.html",{"type":"debug"})
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
        payload = json.loads(params.replace("'","\""))# 参数字符串转json串
        req_type = request.POST.get("req_type")# 请求类型form-data/JSON
        req_headers = request.POST.get("req_header")
        # print("headers====",req_headers)
        headers = json.loads(req_headers.replace("'","\""))

        #判断请求方法
        if method == "get":
            # payload = {'key1': 'value1', 'key2': 'value2'}# 参数形式为key:value形式
            r = requests.get(url,headers=headers, params=payload)

        elif method == "post":
            # 判断参数类型req_type：form-data /JSON
            print("req_type===========",req_type)
            if req_type == "JSON":
                r = requests.post(url, headers=headers, data=json.dumps(payload))
            elif req_type == "form":
                r = requests.post(url,headers=headers, data=payload)
                print("r.url=== ", r.url,)


    return HttpResponse(r.text)
