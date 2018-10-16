from django import forms

class ProjectForm(forms.Form):
    """
    定义项目修改页面表单
    """
    pname = forms.CharField(label="项目名称",max_length=255)
    description = forms.CharField(label="描述",max_length=255)
    status = forms.BooleanField(label="状态",required=False)