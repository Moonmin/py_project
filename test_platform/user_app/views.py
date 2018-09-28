from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth

# Create your views here

def index(request):
    return render(request,'index.html')

#处理登录请求
def login_action(request):
    #获取请求的方法是否为POST
    if request.method == 'POST':
        #默认赋空值
        user_name = request.POST.get('user_name','')
        user_pwd = request.POST.get('password','')
        print("user_name",user_name)
        print("user_pwd",user_pwd)
        if(user_name == '' or user_pwd == ''):
            #当用户名或密码为空时，跳转回登录页面,并给出提示
            return render(request,'index.html',
                          {'error':'用户名或密码为空'})

        else:
            #如果用户名密码不为空，则到数据库校验
            user_name = auth.authenticate(username=user_name,password=user_pwd) #用户认证
            if user_name != None:
                # 如果数据返回值不为None,说明登录信息正确，
                auth.login(request,user_name)   # 负责用户登录状态的保持，将用户保存在session中
                return render(request, 'success.html', {'user_name': user_name})#跳转登录页面
            else:
                # 如果数据返回值为None,说明用户或密码错误，跳回登录页
                return render(request, 'index.html',
                              {'error': '用户名或密码错误'})


