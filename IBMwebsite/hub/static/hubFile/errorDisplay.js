
        function clearmsg(){
			var t = setTimeout(function(){
			$("#msg").remove();
			},2000)
		};
		function alertNo(){
			var h = "不存在der"
			$("body").append("<div id='msg'><span>"+h+"</span></div>");
			clearmsg();
		}
		function disp_alert(h){
			$("body").append("<div id='msg'><span>"+h+"</span></div>");
			clearmsg();
		}

        switch(List[0])
        {
        case  "您使用了与别人相同的用户名！":
            disp_alert(List);
            break;
        case  "密码或用户名错误!":
            disp_alert(List);
            break;
        case  "您在试图创建重复名字的项目！":
            disp_alert(List);
            break;
        default:
            alert("Dangerous action!");
            break;
        }