//获取指定caseid的用例信息
var caseInit = function (case_id)
{
    //window.alert(case_id)
    function getCaseInfo()
    {
        $.post("/interface/get_case_info/",
            {"caseId": case_id,},
            function (resp)
            {
                if(resp.success === "true")
                {
                    //如果查询结果返回success,结果写入各个element中
                    let resp_result = resp.data;
                    console("resp_result", resp_result)
                }
            }
            );
    }
    //调用getCaseInfo 函数，获取修改初始化数据
    getCaseInfo();
}





