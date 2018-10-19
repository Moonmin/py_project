from django import forms
from .models import Project

class ProjectForm(forms.Form):
    """
    定义项目管理页面表单
    """
    pname = forms.CharField(label="项目名称",max_length=255)
    description = forms.CharField(label="描述",widget=forms.Textarea(attrs={"class": "form-control"}))
    status = forms.BooleanField(label="状态",required=False)

    # class Meta:
    #     #定义模型的元数据
    #     model = Project
    #     exclude = ("create_time")#排除create_time，不会显示在页面上

    # def __init__(self, *args, **kwargs):
    #     super(ProjectForm, self).__init__(*args, **kwargs)
    #     for fieldname in self.base_fields:  # 循环给所有字段加样式
    #         field = self.base_fields[fieldname]
    #         field.widget.attrs.update({'class': 'form-control'})