# test-dev06前后端代码重构

## 重构应用

1. 为了项目结构清晰，易维护，可以把现在有项目应用user_app拆分成多个应用（可根据功能维度来划分），如下：

   - user_app:用户管理
   - project_app:项目、模块管理
   - interface_app:接口、用例管理
   - tools_app:测试工具

   2.重构步骤

   创建新应用project_app

   ```
   python manage.py  startapp project_app
   ```

   修改setting.py,添加新应用

   ```
   project_app.apps.ProjectAppConfig
   ```

   移除user_app/admin.py至project_app下

   移除user_app/models.py至project_app下

   移除user_app/views.py中项目管理相关方法至project_app下



   重新执行python manage.py  makemigrations，生成迁移文件

   ```
   Migrations for 'project_app':
     project_app\migrations\0001_initial.py
       - Create model Module
       - Create model Project
       - Add field project to module
   Migrations for 'user_app':
     user_app\migrations\0003_auto_20181015_1609.py
       - Remove field project from module
       - Delete model Module
       - Delete model Project
   ```


执行python manage.py migrate，生成新的表结构

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, project_app, sessions, user_app
Running migrations:
  Applying project_app.0001_initial... OK
  Applying user_app.0003_auto_20181015_1609... OK
```

新增url.py

 在project_app下新增url.py用于管理project_app下的二级url

修改项目的urls.py，登录后项目管理页面请求指定二级目录

```
 path("manage/",include("project_app.urls"))

```



## 重构样式

新建base.html公用样式文件，其它页面可引用

## 优化增、删、改功能

能页面模板中，通过django的标签控制同一个页面不同的功能展示，无需为增、改功能创建新页面



******************





## 问题

1. project_manage继承base.html页面，base.html同时引入bootstrap.min.css、signin.css，project_manage继承后，表格样式冲突

   原因：project_manage的form是从登录页面login.html 复制过来的,form表单引入form-singin样造成表格样式冲突，先前由于project_manage页面未引入signin.css（现继承signin.css）, class="form-signin" 未生效，所以未发现此问题

   ```
   project_manage.html form 中引入了以样式
   
   <form class="form-signin" action="/login_action/" method="post">
   ```

   解决办法：删除form上的样式