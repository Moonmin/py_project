from django.shortcuts import render
from django.http import Http404

# Create your views here.

def case_manage(request):
    if request.method == "GET":
        return render(request, "case_manage.html",{"type":"list"})
    else:
        return Http404("页面不存在！")

def api_debug(request):
    if request.method == "GET":
        return render(request, "api_debug.html",{"type":"debug"})
    else:
        return Http404("请求错误！")