from django.shortcuts import render
from django.http import HttpResponse
# Create your views here

def index(request):
    return render(request,'index.html')

#处理登录请求
def login_action(request):
    #获取请求的方法是否为GET
    if request.method == 'GET':
        user_name = request.GET.get('user_name')
        user_pwd = request.GET.get('password')
        if(user_name == '' or user_pwd == ''):
            #当用户名或密码为空时，跳转回登录页面,并给出提示
            return render(request,'index.html',
                          {'error':'用户名或密码为空'})

