from django.shortcuts import render
from django.http import Http404

# Create your views here.
def task_manage(request):
    if request.method == "GET":
        return render(request, "task_manage.html")
    else:
        return Http404("请求错误！")


