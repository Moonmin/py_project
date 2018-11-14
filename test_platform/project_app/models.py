from django.db import models

# Create your models here.

# 项目表


class Project(models.Model):
    # id = models.AutoField(primary_key=True)# 会默认生成
    pname = models.CharField("名称",max_length=255,blank=False,default="")
    description = models.CharField("描述",max_length=255,default="")
    status = models.BooleanField("状态",default=True)
    create_time = models.DateTimeField("创建时间",auto_now=True)

    def __str__(self):
        return self.pname


class Module(models.Model):
    """
    模块表
    """
    # 当关联的project删除时，对应的module也删除
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    mname = models.CharField("名称",max_length=255,blank=False,default="")
    description = models.CharField("描述", max_length=255, default="")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.mname