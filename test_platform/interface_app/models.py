from django.db import models
from project_app.models import Module
from django.contrib.auth.models import User

# Create your models here.


class TestCase(models.Model):
    """
    用例模型
    当需要限制最大长度时，使用CharField，否则为TextField
    """

    module = models.ForeignKey(Module,on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=255, blank=False, default="")
    url = models.CharField("URL", max_length=100, default="")
    req_method = models.CharField("请求方法", max_length=10, default="")
    req_type = models.CharField("请求类型", max_length=10, default="")
    req_header = models.TextField("Header", default="")
    req_param = models.TextField("请求参数", default="")
    rsp_assert = models.TextField("验证", default="")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    # 删除的时候，外键字段被设置为空，前提就是blank=True, null=True,定义该字段的时候，允许为空。
    creator = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
