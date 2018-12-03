from django import forms
from .models import TestCase

class TestCaseForm (forms.ModelForm):
    """
    定义用例管理页面表单
    """
    # module_name = forms.CharField(label="模块名称",max_length=255)

    class Meta:
        # 定义模型的元数据
        model = TestCase
        fields = ['module','creator']
