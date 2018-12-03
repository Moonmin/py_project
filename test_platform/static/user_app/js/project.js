//初始化
var ProjectInit = function(_cmbProject, _cmbModule, defaultProject, defaultModule)
{
    //获取页面项目和模型2个元素
    //console.log("222222222222")
    var cmbProject = document.getElementById(_cmbProject);
    var cmbModule = document.getElementById(_cmbModule);
    var dataList = [];


    //设置默认选项,修改页面数据回填
    function cmbSelect(cmb, str) {
        for(var i=0; i< cmb.options.length; i++)
        {
            if(cmb.options[i].value == str)
            {
                //console.log("3222222222s")
                cmb.selectedIndex = i;
                return;
            }
        }
    }
    //创建下拉选项
    function cmbAddOption(cmb, str, obj)
    {

        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = str;
        option.value = str;
        option.obj = obj;
    }

    //项目变更，查询对应的模块数据生成下拉列表
    function changeProject() {
        cmbModule.options.length = 0;
        //cmbModule.onchange = null;
        if (cmbProject.selectedIndex == -1)
        {
            return;
        }
        var item = cmbProject.options[cmbProject.selectedIndex].obj;
        //console.log(item)
        for (var i = 0; i < item.moduleList.length; i++)
        {
            cmbAddOption(cmbModule, item.moduleList[i], null);
        }

        cmbSelect(cmbModule, defaultModule);
    }

    function getProjectList()
    {
        // 调用项目服务列表接口
        $.get("/interface/get_project_list", {}, function (resp)
        {
            if(resp.success === "true"){
                dataList = resp.data;
                //遍历项目
                for (var i = 0; i < dataList.length; i++)
                {
                    //console.log("1",dataList[i]["pname"])
                    //console.log("2",dataList[i]["moduleList"])
                    //console.log("3",dataList[i].moduleList[0])
                    cmbAddOption(cmbProject, dataList[i].name, dataList[i]);
                }

                cmbSelect(cmbProject, defaultProject);
                changeProject();
                cmbProject.onchange = changeProject;
            }

            cmbSelect(cmbProject, defaultProject);
            //$("#result").html(resp);
        });
    }
    // 调用getProjectList函数
    getProjectList();

};

