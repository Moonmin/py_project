import json
import requests
from test_platform import common
from interface_app.models import TestCase
from project_app.models import Project, Module


def get_case_info(request):
    """
    根据case_id，获取用例信息，用于用例修改初始化数据
    :param request:
    :return:
    """
    if request.method == "POST":
        case_id = request.POST.get("caseId")
        if(case_id == ""):
            return

    return ""