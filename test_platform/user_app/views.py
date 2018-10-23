from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

# Create your views here

def index(request):
    return render(request, 'login.html')

#处理登录请求
def login_action(request):
    #获取请求的方法是否为POST
    if request.method == 'POST':
        #默认赋空值
        user_name = request.POST.get('user_name','')
        user_pwd = request.POST.get('password','')
        # print("user_name",user_name)
        # print("user_pwd",user_pwd)
        if(user_name == '' or user_pwd == ''):
            #当用户名或密码为空时，跳转回登录页面,并给出提示
            return render(request, 'login.html',
                          {'error':'用户名或密码为空'})

        else:
            #如果用户名密码不为空，则到数据库校验
            user_name = auth.authenticate(username=user_name,password=user_pwd) #用户认证
            if user_name != None:
                # 如果数据返回值不为None,说明登录信息正确，
                auth.login(request,user_name)   # 负责用户登录状态的保持，将用户保存在session中
                #return render(request, 'index.html', {'user_name': user_name})#跳转登录页面
                #存储用户名到cookie中
                # response.set_cookie("cuser_name",user_name,3600)
                #对应用户名存入cookie的另一种方式，存入session表中
                print("user_name111=", user_name)
                request.session['cuser_name'] = user_name

                # 重定向请求
                return HttpResponseRedirect("/manage/project_manage/")
            else:
                # 如果数据返回值为None,说明用户或密码错误，跳回登录页
                return render(request, 'login.html',
                              {'error': '用户名或密码错误'})


'''
从session里面读取用户信息  
重定向请求跳转至新页面
'''

#退出功能
def logout(request):
    auth.logout(request) #清除用户登录状态
    return HttpResponseRedirect("/") #重定向至登录页面


'''@login_required
def project_manage(request):
    # cuser_name = request.COOKIES.get("cuser_name","")
    # print("cuser_name=",cuser_name)
    cuser_name = request.session.get("cuser_name","")
    latest_project_list = Project.objects.all()
    #print("latest_project_id=",latest_project_list.get(pname="项目1"))
    #context = {"latest_project_list":latest_project_list}

    return render(request,"project_manage.html",{"cuser_name":cuser_name,"latest_project_list":latest_project_list})

#退出功能
def logout(request):
    auth.logout(request) #清除用户登录状态
    return HttpResponseRedirect("/") #重定向至登录页面

#新增项目
def add_project(request):
    if request.method == 'POST':
        #print("POSTPOSTPOST")
        #新增提交
        pname = request.POST.get("pname")
        description = request.POST.get("description")
        status = request.POST.get("status","False")
        #print("status=",status)
        Project.objects.create(pname=pname,description=description,status=status)
        #跳转回首页
        return HttpResponseRedirect("/project_manage/")
    elif request.method == "GET":
        #跳转新增页面
        return render(request, "project_manage_add.html")

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
'''